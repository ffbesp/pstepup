
from pstepup import probabilitycalc, appdata


def test_expected_value():
    rates_and_pulls = { 1 : 1, 0.03 : 100 }
    assert probabilitycalc.expected_value(rates_and_pulls) == 4
    
    actual = probabilitycalc.expected_value({ 0.25 : 1, 0.01 : 9, 0.02 : 4, 0.015 : 1, 0.05 : 10 })
    assert round(actual, 3) == 0.935


def test_prob_for_exactly_x():
    assert probabilitycalc.prob_for_exactly_x(0.03, 1) == { 0 : 0.97, 1 : 0.03 }
    assert probabilitycalc.prob_for_exactly_x(1.0, 1) == { 0 : 0, 1 : 1 }
    assert probabilitycalc.prob_for_exactly_x(1.0, 4) == { 0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 1 }

    actual = { k:round(v,7) for k,v in probabilitycalc.prob_for_exactly_x(0.02, 4).items() }
    assert actual == { 0 : 0.9223682, 1 : 0.0752954, 2 : 0.002305, 3 : 0.0000314, 4 : 0.0000002 }

    actual = { k:round(v,11) for k,v in probabilitycalc.prob_for_exactly_x(0.01, 7).items() }
    assert actual == { 0 : 0.93206534791, 1 : 0.06590361046, 2 : 0.0019970791, 3 : 0.00003362086, 4 : 0.0000003396, 5 : 0.00000000206 }


def test_at_least_x():
    prob_exactly_x = { 0 : 0.15, 1 : 0.45, 2 : 0.25, 3 : 0.10, 4 : 0.05 }
    at_least_x = { k:round(v,5) for k,v in probabilitycalc.at_least_x(prob_exactly_x).items() }
    expected = { 0 : 1.0, 1 : 0.85, 2 : 0.4, 3 : 0.15, 4 : 0.05 }
    
    assert at_least_x == expected


def test_aggregating_prob_exactly_x():
    prob_dict = { 0.03 : { 0 : 0.55, 1 : 0.35, 2 : 0.10 }, 0.05 : { 0 : 0.95, 1 : 0.05 } }
    agg_prob_exactly_x = { k:round(v,5) for k,v in probabilitycalc.aggregate_prob_exactly_x(prob_dict).items() }
    expected = { 0 : 0.5225, 1 : 0.36, 2 : 0.1125, 3 : 0.005 }

    assert agg_prob_exactly_x == expected

    prob_dict = { 1.0 : { 0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 1 }, 0.05 : { 0 : 0.95, 1 : 0.05 } }
    actual = { k:round(v,5) for k,v in probabilitycalc.aggregate_prob_exactly_x(prob_dict).items() }

    assert actual == { 0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0.95, 5 : 0.05 }
    