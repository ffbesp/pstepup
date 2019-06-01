

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
    expected_value = 0
    for rate, pull_count in rates_and_pulls.iteritems():
        expected_value += rate * 1000000 * pull_count / 1000000
    return expected_value


def binom_dist(k, p, n):
    """Probability from PMF of binomial distribution

    Probability for exactly k rainbows = p^k * (1 - p)^(n - k) * BC

    Args:
        k (int): number of successes (exactly x)
        p (float): rate of success of a pull
        n (int): number of trials (pull count)

    Returns:
        Float of probability for exactly k successes (rainbows)
    """
    return pow(p, k) * pow(1 - p, n - k) * scipy.special.binom(n, k)


def prob_for_exactly_x(rate, pull_count):
    """Finds probability that pull_count at the rate result in various successful outcomes of x (0,1,2,etc.)

    Args:
        rate (float): rate of success for experiment.
        pull_count (int): number of attempts
    
    Returns:
        Dictionary with x values as key and success rates as values

    Examples:
        exactly_x = { 0 : 0.213, 1 : 0.357, 2 : 0.125 }
    """
    return { x:binom_dist(x, rate, pull_count) for x in range(pull_count+1) if binom_dist(x, rate, pull_count) >= 0.0000000001 or binom_dist(x, rate, pull_count) == 0 }


def aggregate_prob_exactly_x(exactly_x_by_rate):
    """Merge together probability dictionaries to find overall probability to pull x rainbows
    
    Returns:
        Dictionary with x values as key and overall success rates as values

    Examples:
        overall_prob = { 0 : 0.213, 1 : 0.357, 2 : 0.125 }
    """
    rates_by_len_desc = sorted(exactly_x_by_rate, key=lambda k: len(exactly_x_by_rate[k]), reverse=True)

    #create all possible combinations like { (0,1,0) : [0.035, 0.05, 0.70] }
    for idx, rate in enumerate(rates_by_len_desc):
        if idx == 0: #start with longest list
            prob_matrix = exactly_x_by_rate[rate]
        elif idx == 1: #create tuples as keys, lists as values
            prob_matrix = { (x1,x2):[prob1,prob2] for x1, prob1 in prob_matrix.iteritems() for x2, prob2 in exactly_x_by_rate[rate].iteritems() }
        else:
            prob_matrix = { x_tuple + (x2,):prob_list + [prob2] for x_tuple, prob_list in prob_matrix.iteritems() for x2, prob2 in exactly_x_by_rate[rate].iteritems() }

    #aggregate probability for exactly x rainbows; sum tuple keys for X, multiply values list for probability
    prob_for_exactly = {}
    for x_tuple, prob_list in prob_matrix.iteritems():
        exactly_x = sum(x_tuple)
        if exactly_x in prob_for_exactly:
            prob_for_exactly[exactly_x] += reduce(lambda a, b: a*b, prob_list) #multiply values and add to probability for exactly X
        else:
            prob_for_exactly[exactly_x] = reduce(lambda a, b: a*b, prob_list)

    #discard very unlikely probabilities
    return { k:v for k, v in prob_for_exactly.iteritems() if v >= 0.0000000001 or v == 0 }


def at_least_x(exactly_x):
    """Take a dictionary of probabilities for exactly X rainbows and find probability for at least X rainbows
    
    Returns:
        Dictionary with x values as key and probability for at least X successes as values

    Examples:
        print at_least_x( { 0 : 0.3, 1 : 0.4, 2 : 0.15, 3 : 0.15 } ) 
        > { 0 : 1.0, 1 : 0.7, 2 : 0.3, 3: 0.15 }
    """
    total = 1.0
    at_least_x = {}
    for key in sorted(exactly_x):
        at_least_x[key] = total
        total -= exactly_x[key]

    return at_least_x


def get_prob_at_least_x(rates_and_pulls):
    """For a dictionary with rates as key and pulls as value, calculates overall probability to pull at least X rainbows

    Combines steps of: run prob_for_exactly_x for all rates, aggregate probabilities, and find at_least_x for results
    
    Returns:
        Dictionary with x values as key and probability for at least X successes as values

    Examples:
        print get_prob_at_least_x( { 0.03 : 10, 0.05 : 1 } ) 
        > { 0 : 1.0, 1 : 0.299447, 2 : 0.0459100, 3: 0.0043520, ... }
    """
    prob_for_x = { rate:prob_for_exactly_x(rate, pull_count) for rate, pull_count in rates_and_pulls.iteritems() }
    return at_least_x(aggregate_prob_exactly_x(prob_for_x))