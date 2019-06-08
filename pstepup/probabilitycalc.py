"""Functions to calculate probability for rate/pull combinations
"""

from functools import reduce

import scipy.special


def expected_value(rates_and_pulls):
    """Calculates expected value for a dictionary with rates as key and pulls as value

    Returns:
        Float as the expected value

    Examples:
        rates_and_pulls = { 1 : 1, 0.03 : 100 }
        print expected_value(rates_and_pulls)
        > 4
    """
    exp_val = 0
    for rate, pull_count in rates_and_pulls.items():
        exp_val += rate * 1000000 * pull_count / 1000000
    return exp_val


def binom_dist(k, p, n):
    """Probability from PMF of binomial distribution

    Probability for exactly k = p^k * (1 - p)^(n - k) * BC

    Args:
        k (int): number of successes (exactly x)
        p (float): rate of success of a pull
        n (int): number of trials (pull count)

    Returns:
        Float of probability for exactly k successes (rainbows)
    """
    return pow(p, k) * pow(1 - p, n - k) * scipy.special.binom(n, k)


def prob_for_exactly_x(rate, pulls):
    """Probability that pulls at rate results in various successful outcomes of x (0,1,2,etc)

    Args:
        rate (float): rate of success for experiment.
        pulls (int): number of attempts

    Returns:
        Dictionary with x values as key and success rates as values

    Examples:
        exactly_x = { 0 : 0.213, 1 : 0.357, 2 : 0.125 }
    """
    return {
        x:binom_dist(x, rate, pulls)
        for x in range(pulls+1)
        if binom_dist(x, rate, pulls) >= 0.0000000001 or binom_dist(x, rate, pulls) == 0
    }


def aggregate_prob_exactly_x(exactly_x_by_rate):
    """Merge together probability dictionaries to find overall probability to pull X

    Returns:
        Dictionary with x values as key and overall success rates as values

    Examples:
        overall_prob = { 0 : 0.213, 1 : 0.357, 2 : 0.125 }
    """
    rates_by_len_desc = (
        sorted(exactly_x_by_rate, key=lambda k: len(exactly_x_by_rate[k]), reverse=True))

    #create all possible combinations like { (0,1,0) : [0.035, 0.05, 0.70] }
    for idx, rate in enumerate(rates_by_len_desc):
        if idx == 0: #start with longest list
            prob_matrix = exactly_x_by_rate[rate]
        elif idx == 1: #create tuples as keys, lists as values
            prob_matrix = {
                (x1, x2):[prob1, prob2]
                for x1, prob1 in prob_matrix.items()
                for x2, prob2 in exactly_x_by_rate[rate].items()
            }
        else:
            prob_matrix = {
                x_tuple + (x2,):prob_list + [prob2]
                for x_tuple, prob_list in prob_matrix.items()
                for x2, prob2 in exactly_x_by_rate[rate].items()
            }

    #aggregate prob for exactly x; sum tuple keys for X, multiply values list for probability
    prob_for_exactly = {}
    for x_tuple, prob_list in prob_matrix.items():
        exactly_x = sum(x_tuple)
        if exactly_x in prob_for_exactly: #multiply values and add to probability for exactly X
            prob_for_exactly[exactly_x] += reduce(lambda a, b: a*b, prob_list)
        else:
            prob_for_exactly[exactly_x] = reduce(lambda a, b: a*b, prob_list)

    #discard very unlikely probabilities
    return {k:v for k, v in prob_for_exactly.items() if v >= 0.0000000001 or v == 0}


def at_least_x(exactly_x):
    """For dictionary of probabilities for exactly X, find probability for at least X

    Returns:
        Dictionary with x values as key and probability for at least X successes as values

    Examples:
        print at_least_x({ 0 : 0.3, 1 : 0.4, 2 : 0.15, 3 : 0.15 })
        > { 0 : 1.0, 1 : 0.7, 2 : 0.3, 3: 0.15 }
    """
    total = 1.0
    at_least = {}
    for key in sorted(exactly_x):
        at_least[key] = total
        total -= exactly_x[key]

    return at_least


def get_prob_at_least_x(rates_and_pulls):
    """Calculates overall probability to pull at least X

    Executes intermediate steps of: run prob_for_exactly_x for all rates
    , aggregate probabilities, and find at_least_x for results

    Args:
        rates_and_pulls (dict): rates as key, pulls as value

    Returns:
        Dictionary with x values as key and probability for at least X successes as values

    Examples:
        print get_prob_at_least_x({ 0.03 : 10, 0.05 : 1 })
        > { 0 : 1.0, 1 : 0.299447, 2 : 0.0459100, 3: 0.0043520, ... }
    """
    prob_for_x = {rate:prob_for_exactly_x(rate, pulls) for rate, pulls in rates_and_pulls.items()}
    return at_least_x(aggregate_prob_exactly_x(prob_for_x))


def get_prob_exactly_x(rates_and_pulls):
    """Calculates overall probability to pull exactly X

    Executes intermediate steps of: run prob_for_exactly_x for all rates
    and aggregate probabilities

    Args:
        rates_and_pulls (dict): rates as key, pulls as value

    Returns:
        Dictionary with x values as key and probability for exactly X successes as values

    Examples:
        print get_prob_exactly_x({ 0.03 : 10, 0.05 : 1 })
        > { 0 : 0.70055, 1 : 0.253537, 2 : 0.041558, 3: 0.004074, ... }
    """
    prob_for_x = {rate:prob_for_exactly_x(rate, pulls) for rate, pulls in rates_and_pulls.items()}
    return aggregate_prob_exactly_x(prob_for_x)
