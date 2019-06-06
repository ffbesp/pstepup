
import copy

from pstepup import stepupbanner, appdata


def test_setting_ex_rainbow_rates():
    banner_info = { 'bannerRainbowCount' : 1, 'fiveStarBaseUnitCount' : 20, 'totalAvailableLaps' : 1, 'steps' : { '1' : { 'summons' : { 'guaranteedGold' : 1, 'regular' : 10 } } } }
    pull_types_and_rates = stepupbanner.StepUpBanner(appdata.pull_type, banner_info)
    assert pull_types_and_rates.base_rates['guaranteedEXRainbow']['bannerRainbowRate'] == 0.05


def test_all_pulls_accounted_for():
    banner_info = { 'bannerRainbowCount' : 1, 'totalAvailableLaps' : 1, 'fiveStarBaseUnitCount' : 40, 'steps' : { '1' : { 'summons' : { 'guaranteedGold' : 1, 'regular' : 10 } }, '2' : { 'summons' : { 'guaranteedGold' : 1, 'regular' : 10 } } } }
    total_pulls, expected_pulls = 0, 0
    errors = []

    step_up = stepupbanner.StepUpBanner(copy.deepcopy(appdata.pull_type), banner_info)

    for step_number, step_data in banner_info['steps'].items():
        for pull_type, pull_count in step_data['summons'].items():
            expected_pulls += pull_count

    for name, rate_dict in step_up.rates_and_pulls_per_lap.items():
        for key, value in rate_dict.items():
            total_pulls += value
        if total_pulls != expected_pulls:
            errors.append(name + ': unexpected pull count (' + str(total_pulls) + ') vs expected count (' + str(expected_pulls) + ')' )
        total_pulls = 0

    assert not errors, 'errors occured:\n{}'.format('\n'.join(errors))


def test_no_rates_greater_than_100():
    banner_info = { 'bannerRainbowCount' : 1, 'totalAvailableLaps' : 1, 'fiveStarBaseUnitCount' : 100, 'steps' : { '1' : { 'summons' : { 'guaranteedGold' : 1, 'regular' : 10 } }, '2' : { 'bonusBannerFiveStarRate' : 5, 'summons' : { 'guaranteedGold' : 1, 'regular' : 9, 'guaranteedRainbowWithRateUp' : 1 } } } }

    expected_general_rates_and_pulls = { 0.03 : 10, 0.05 : 1, 0.2 : 1, 0.07 : 9, 1.0 : 1 }
    expected_banner_rates_and_pulls = { 0.01 : 10, 0.0375 : 1, 0.1875 : 1, 0.05 : 9, 0.25 : 1 }
    expected_oneunit_rates_and_pulls = expected_banner_rates_and_pulls

    step_up = stepupbanner.StepUpBanner(copy.deepcopy(appdata.pull_type), banner_info)

    assert expected_general_rates_and_pulls == step_up.rates_and_pulls_per_lap['general']
    assert expected_banner_rates_and_pulls == step_up.rates_and_pulls_per_lap['banner'] 
    assert expected_oneunit_rates_and_pulls == step_up.rates_and_pulls_per_lap['oneunit']


def test_sum_pulls_for_rates():
    banner_info = { 'bannerRainbowCount' : 1, 'totalAvailableLaps' : 1, 'fiveStarBaseUnitCount' : 100, 'steps' : { '1' : { 'summons' : { 'guaranteedGold' : 1, 'regular' : 10 } }, '2' : { 'summons' : { 'guaranteedGold' : 1, 'regular' : 10 } } } }
    rates_and_pulls = stepupbanner.sum_pulls_for_rates(copy.deepcopy(appdata.pull_type), banner_info)

    assert rates_and_pulls['general'] == { 0.03 : 20, 0.05 : 2 }
    assert rates_and_pulls['banner'] == { 0.01 : 20, 0.0375 : 2 }
    assert rates_and_pulls['oneunit'] == { 0.01 : 20, 0.0375 : 2 }

    two_laps = { type_rate: { rate:pull*2 for rate, pull in r_and_p.items() } for type_rate, r_and_p in rates_and_pulls.items() }

    assert two_laps['general'] == { 0.03 : 40, 0.05 : 4 }
    assert two_laps['banner'] == { 0.01 : 40, 0.0375 : 4 }
    assert two_laps['oneunit'] == { 0.01 : 40, 0.0375 : 4 }

    banner_info['bannerRainbowCount'] = 2
    multi_banner = stepupbanner.sum_pulls_for_rates(copy.deepcopy(appdata.pull_type), banner_info)

    assert multi_banner['oneunit'] == { 0.005 : 20, 0.01875 : 2 }
