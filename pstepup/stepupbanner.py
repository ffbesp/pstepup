"""StepUpBanner class and related utility functions
"""

import copy

FIVE_PERCENT_RAINBOW_RATE_BANNERS = [
    'Yuffie 24K', 'Zack 24K', 'Elena/Morgana 24K', 'Rivera 12K', 'R. Lightning/N. Hope 25K',
    'Riku/KH Sephiroth 24K', 'Sora/KHloud 20K'
]
FIVE_TIMES_RATE_G_RAINBOW_BANNERS = [
    'Nagi 12K', 'Yego 12K', 'Crimson 12K', 'Karlette 12K', 'Yuraisha 12K', 'Cid 12K'
]
FEATURED_UNIT_SHARING_RATEUP_BANNERS = [
    'Galuf 24K', 'Krile 24K', 'Exdeath 24K'
]

def get_custom_rates(banner_name):
    """Returns custom rates that apply to all pulls on step-up banner

    Necessary for step-ups with abnormal base rates e.g. SS Charlotte banner featuring
    5% rainbow rates

    Returns:
        A tuple of regular and guaranteedGold rates

    Examples:
        regular, gold = get_custom_rates('SS Charlotte 24K')
    """
    if banner_name == 'SS Charlotte 24K':
        regular = {
            'rainbowRate' : 0.05,
            'bannerRainbowRate' : 0.015,
            'offBannerRainbowRate' : 0.035
        }
        guaranteedGold = {
            'rainbowRate' : 0.07,
            'bannerRainbowRate' : 0.056,
            'offBannerRainbowRate' : 0.014
        }
        return (regular, guaranteedGold)
    elif banner_name == 'Karten/Godrea 24K':
        regular = {
            'rainbowRate' : 0.05,
            'bannerRainbowRate' : 0.015,
            'offBannerRainbowRate' : 0.035
        }
        guaranteedGold = {
            'rainbowRate' : 0.07,
            'bannerRainbowRate' : 0.05625,
            'offBannerRainbowRate' : 0.01375
        }
        return (regular, guaranteedGold)
    elif banner_name in FIVE_PERCENT_RAINBOW_RATE_BANNERS:
        regular = {
            'rainbowRate' : 0.05,
            'bannerRainbowRate' : 0.01,
            'offBannerRainbowRate' : 0.04
        }
        guaranteedGold = {
            'rainbowRate' : 0.07,
            'bannerRainbowRate' : 0.0375,
            'offBannerRainbowRate' : 0.0325
        }
        return (regular, guaranteedGold)
    elif banner_name in FEATURED_UNIT_SHARING_RATEUP_BANNERS:
        regular = {
            'rainbowRate' : 0.03,
            'bannerRainbowRate' : 0.005,
            'offBannerRainbowRate' : 0.025
        }
        guaranteedGold = {
            'rainbowRate' : 0.05,
            'bannerRainbowRate' : 0.01875,
            'offBannerRainbowRate' : 0.03125
        }
        return (regular, guaranteedGold)


def special_case_rates(pull_type, rate_up_multiplier, banner_name):
    """Check for scenarios with special case pull rates, and return new rates if necessary

    Necessary for several banner rate-ups that do not follow the normal rules
    e.g. GLEX 12K banners starting with Cid have 25% banner rate on Step 5 while advertising
    '5x banner rate-up', BM Golbez with 10% banner rate on Step 5 with '3x banner rate-up'

    Returns:
        A tuple of banner rate and off-banner rate if special case exists, else None

    Examples:
        banner_rate, off_banner_rate = special_case_rates('bannerRainbowRate', 1.0, 'Cid 12K')
    """
    if (pull_type == 'guaranteedRainbowWithRateUp' and rate_up_multiplier == 3 and 
        banner_name == 'BM Golbez 10K'):
        return (0.10, 0.90) #BM Golbez: 10% on banner, 90% off
    elif (pull_type == 'guaranteedRainbowWithRateUp' and rate_up_multiplier == 5 and 
        banner_name in FIVE_TIMES_RATE_G_RAINBOW_BANNERS):
        return (0.25, 0.75) #Cid: 25% on banner, 75% off
    elif (pull_type == 'regular' and rate_up_multiplier == 1.5 and banner_name == 'Rivera 12K'):
        return (0.015, 0.035) #Rivera step 1 and 2: 1.5% on banner, 3.5% off
    elif (pull_type == 'guaranteedGold' and rate_up_multiplier == 1.5 and 
        banner_name in ['Rivera 12K', 'Chocobo Fina 21K']):
        return (0.05625, 0.01375) #Rivera step 1 and 2: 5.625% on banner, 1.375% off
    elif (pull_type == 'regular' and rate_up_multiplier == 2 and banner_name == 'Rivera 12K'):
        return (0.02, 0.03) #Rivera step 3: 2% on banner, 3% off
    elif (pull_type == 'guaranteedGold' and rate_up_multiplier == 2 and 
        banner_name in ['Rivera 12K', 'AI Katy 10K']):
        return (0.075, 0.0125) #Rivera step 3, AI Katy step 1: 7.5% on banner, 1.25% off
    elif (pull_type == 'regular' and rate_up_multiplier == 2 and banner_name == 'AI Katy 10K'):
        return (0.02, 0.01) #AI Katy step 1: 2% on banner, 1% off
    elif (pull_type == 'regular' and rate_up_multiplier == 1.5 and 
        banner_name == 'Chocobo Fina 21K'): #Choco Fina step 2 and 4: 1.5% on, 1.5% off
        return (0.015, 0.015)
    else:
        return None


def sum_pulls_for_rates(rates, banner_info):
    """For set of base rates and step-up banner, aggregate number of pulls available at each rate

    Returns:
        A dictionary with 3 sub-dictionaries, each having rates as key and pull count as value;
        sub-dictionaries have rates for Rainbows in general ('general'), rates for on-banner
        Rainbows only ('banner'), and rates for one specific banner Rainbow only ('oneunit')

    Examples:
        print sum_pulls_for_rates(basic_rates, two_ten_plus_one_single_rainbow_banner)
        > { 'general' : { 0.03 : 20, 0.05 : 2 }, 'banner' : { 0.01 : 20, 0.0375 : 2 },
        'oneunit' : { 0.01 : 20, 0.0375 : 2 } }
    """
    rates_and_pulls = {'general' : {}, 'banner' : {}, 'oneunit' : {}}
    banner_unit_count = banner_info['bannerRainbowCount']
    banner_name = banner_info.get('bannerName')

    for step_data in banner_info['steps'].values():
        general_rate_up = step_data.get('bonusFiveStarRate', 1)
        banner_rate_up = step_data.get('bonusBannerFiveStarRate')
        rate_up_multiplier = banner_rate_up if banner_rate_up is not None else general_rate_up

        for p_type, pull_count in step_data['summons'].items():
            if not special_case_rates(p_type, rate_up_multiplier, banner_name):
                one_unit_banner_rate = (
                    rates[p_type]['bannerRainbowRate'] / banner_unit_count * rate_up_multiplier)
                banner_rate = rates[p_type]['bannerRainbowRate'] * rate_up_multiplier
                off_banner_rate = rates[p_type]['offBannerRainbowRate'] * general_rate_up
            else:
                banner_rate, off_banner_rate = (
                    special_case_rates(p_type, rate_up_multiplier, banner_name))
                one_unit_banner_rate = banner_rate

            general_rate = banner_rate + off_banner_rate

            rates_and_pulls['general'][round(general_rate, 5)] = (
                rates_and_pulls['general'].get(round(general_rate, 5), 0) + pull_count)
            rates_and_pulls['banner'][round(banner_rate, 5)] = (
                rates_and_pulls['banner'].get(round(banner_rate, 5), 0) + pull_count)
            rates_and_pulls['oneunit'][round(one_unit_banner_rate, 5)] = (
                rates_and_pulls['oneunit'].get(round(one_unit_banner_rate, 5), 0) + pull_count)

    return rates_and_pulls


class StepUpBanner:
    """Object representing step-up banner to hold base pull rates and total pulls

    Args:
        p_type (dict): rate name as k, dict as v with rates for on/off banner/total rainbows
        banner_info (dict): number of laps, banner metadata, and step details

    Attributes:
        laps (int): total available laps on step-up banner
        base_rates (dict): rate name as k, dict as v with rates for on/off banner/total rainbows
        rates_and_pulls_per_lap (dict): dictionary with 3 sub-dictionaries, each having
            rates as key and total pull count as value
    """
    def __init__(self, p_type, banner_info):
        self.laps = banner_info['totalAvailableLaps']
        self.set_base_rates(p_type, banner_info)
        self.rates_and_pulls_per_lap = sum_pulls_for_rates(self.base_rates, banner_info)

    def set_base_rates(self, p_type, banner_info):
        """Init base_rates dict for rates applicable to specific banner

        Args:
            p_type (dict): rate name as k, dict as v with rates for on/off banner/total rainbows
            banner_info (dict): number of laps, banner metadata, and step details
        """
        self.base_rates = copy.deepcopy(p_type)
        #set custom rates if applicable
        if banner_info.get('customBannerRates'):
            regular, gold = get_custom_rates(banner_info.get('bannerName'))
            self.base_rates['regular'] = regular
            self.base_rates['guaranteedGold'] = gold
        #account for On Banner only and EX rainbow rate
        if banner_info.get('allRainbowsOnBanner'):
            for pull_rates in self.base_rates.values():
                pull_rates['bannerRainbowRate'] = pull_rates['rainbowRate']
                pull_rates['offBannerRainbowRate'] = 0
        else:
            self.base_rates['guaranteedEXRainbow']['bannerRainbowRate'] = (
                float(banner_info['bannerRainbowCount'])
                / float(banner_info['fiveStarBaseUnitCount']))
            self.base_rates['guaranteedEXRainbow']['offBannerRainbowRate'] = (
                1 - self.base_rates['guaranteedEXRainbow']['bannerRainbowRate'])
