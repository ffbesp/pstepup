
import probabilitycalc


def main():
    #For a single rainbow banner, find probability for at least x banner rainbows on 2x 10+1 pulls
    #rate as key, pull_count as value
    rates_and_pulls = { 0.01 : 20, 0.0375 : 2 }
    print('2x 10+1, single rainbow banner, at least X banner rainbows', probabilitycalc.get_prob_at_least_x(rates_and_pulls), '\n')

    #2x 10+1 pulls on old 5% Nalu banner: 1.667% on regular pull, 6.375% on +1 for Nalu
    rates_and_pulls = { 0.01667 : 20, 0.06375 : 2 }
    print('2x 10+1, Nalu 5% rainbow banner, at least X Nalus', probabilitycalc.get_prob_at_least_x(rates_and_pulls), '\n')

    #2x 10+1 pulls on old 5% Nalu banner, this time probability for any rainbows (general rainbow rate 5%, 8.5% on +1)
    rates_and_pulls = { 0.05 : 20, 0.085 : 2 }
    print('2x 10+1, Nalu 5% rainbow banner, at least X Any Rainbow', probabilitycalc.get_prob_at_least_x(rates_and_pulls), '\n')


if __name__ == '__main__':
    main()