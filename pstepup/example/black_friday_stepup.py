
import probabilitycalc


def main():
    #rate as key, pull_count as value
    rates_and_pulls = { 0.0075 : 18, 0.01875 : 2, 0.01099 : 2 }
    print('1 lap, B. Olive', probabilitycalc.get_prob_at_least_x(rates_and_pulls), '\n')
    print('EV', probabilitycalc.expected_value(rates_and_pulls), '\n')

    rates_and_pulls = { 0.0075 : 36, 0.01875 : 4, 0.01099 : 4, 0.10 : 1 }
    print('2 laps + 20%, B. Olive', probabilitycalc.get_prob_at_least_x(rates_and_pulls), '\n')
    print('EV', probabilitycalc.expected_value(rates_and_pulls), '\n')

    rates_and_pulls = { 0.0075 : 54, 0.01875 : 6, 0.01099 : 6, 0.10 : 1 }
    print('3 laps + 20%, B. Olive', probabilitycalc.get_prob_at_least_x(rates_and_pulls), '\n')
    print('EV', probabilitycalc.expected_value(rates_and_pulls), '\n')

    rates_and_pulls = { 0.0075 : 72, 0.01875 : 8, 0.01099 : 8, 0.50 : 1 }
    print('4 laps + 50/50, B. Olive', probabilitycalc.get_prob_at_least_x(rates_and_pulls), '\n')
    print('EV', probabilitycalc.expected_value(rates_and_pulls), '\n')

    rates_and_pulls = { 0.0075 : 108, 0.01875 : 12, 0.01099 : 12, 0.50 : 1, 0.10 : 1 }
    print('6 laps + 50/50 + 20%, B. Olive', probabilitycalc.get_prob_at_least_x(rates_and_pulls), '\n')
    print('EV', probabilitycalc.expected_value(rates_and_pulls), '\n')

    rates_and_pulls = { 0.0075 : 144, 0.01875 : 16, 0.01099 : 16, 1.0 : 1 }
    print('8 laps + banner UoC, B. Olive', probabilitycalc.get_prob_at_least_x(rates_and_pulls), '\n')
    print('EV', probabilitycalc.expected_value(rates_and_pulls), '\n')


if __name__ == '__main__':
    main()