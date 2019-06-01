
import copy

def special_case_rates(pull_type, rate_up_multiplier):
    """Check for scenarios with special case pull rates, and return new rates if necessary

    Necessary for several banner rate-ups that do not follow the normal rules
    e.g. GLEX 12K banners starting with Cid have 25% banner rate on Step 5 while advertising '5x banner rate-up', 
    BM Golbez with 10% banner rate on Step 5 with '3x banner rate-up'
    
    Returns:
        A tuple of banner rate and off-banner rate if special case exists, else None

    Examples:
        banner_rate, off_banner_rate = special_case_rates('bannerRainbowRate', 1.0)
    """
    if pull_type == 'guaranteedRainbowWithRateUp' and rate_up_multiplier == 3: #BM Golbez: 10% on banner, 90% off
        return (0.10, 0.90)
    elif pull_type == 'guaranteedRainbowWithRateUp' and rate_up_multiplier == 5: #Cid: 25% on banner, 75% off
        return (0.25, 0.75)
    else:
        return None


def sum_pulls_for_rates(rates, banner_info):
    """For a given set of base rates and step-up banner, aggregate the number of pulls available at each rate
    
    Returns:
        A dictionary with 3 sub-dictionaries, each having rates as key and pull count as value; sub-dictionaries
        have rates for Rainbows in general ('general'), rates for on-banner Rainbows only ('banner'), and 
        rates for one specific banner Rainbow only ('oneunit')

    Examples:
        print sum_pulls_for_rates(basic_rates, two_ten_plus_one_single_rainbow_banner)
        > { 'general' : { 0.03 : 20, 0.05 : 2 }, 'banner' : { 0.01 : 20, 0.0375 : 2 }, 'oneunit' : { 0.01 : 20, 0.0375 : 2 } }
    """
    rates_and_pulls = { 'general' : {}, 'banner' : {}, 'oneunit' : {} }
    banner_unit_count = banner_info['bannerRainbowCount']

    for step_number, step_data in banner_info['steps'].iteritems():
        general_rate_up = step_data.get('bonusFiveStarRate', 1)
        banner_rate_up = step_data.get('bonusBannerFiveStarRate')
        rate_up_multiplier = banner_rate_up if banner_rate_up is not None else general_rate_up

        for p_type, pull_count in step_data['summons'].iteritems():
            if not special_case_rates(p_type, rate_up_multiplier):
                one_unit_banner_rate = rates[p_type]['bannerRainbowRate'] / banner_unit_count * rate_up_multiplier
                banner_rate = rates[p_type]['bannerRainbowRate'] * rate_up_multiplier
                off_banner_rate = rates[p_type]['offBannerRainbowRate'] * general_rate_up
            else:
                banner_rate, off_banner_rate = special_case_rates(p_type, rate_up_multiplier)
                one_unit_banner_rate = banner_rate

            general_rate = banner_rate + off_banner_rate

            rates_and_pulls['general'][round(general_rate,5)] = rates_and_pulls['general'].get(round(general_rate,5), 0) + pull_count
            rates_and_pulls['banner'][round(banner_rate,5)] = rates_and_pulls['banner'].get(round(banner_rate,5), 0) + pull_count
            rates_and_pulls['oneunit'][round(one_unit_banner_rate,5)] = rates_and_pulls['oneunit'].get(round(one_unit_banner_rate,5), 0) + pull_count

    return rates_and_pulls


class StepUpBanner:
    """Object representing step-up banner to hold base pull rates and total pulls

    Args:
        p_type (dict): rate name as key, dict as value containing rates for on/off banner and total rainbows
        banner_info (dict): 

    Attributes:
        laps (int): total available laps on step-up banner
        base_rates (dict): rate name as key, dict as value containing rates for on/off banner and total rainbows
        rates_and_pulls_per_lap (dict): dictionary with 3 sub-dictionaries, each having rates as key and 
            total pull count as value
    """
    def __init__(self, p_type, banner_info):
        self.laps = banner_info['totalAvailableLaps']
        self.set_base_rates(p_type, banner_info)
        self.rates_and_pulls_per_lap = sum_pulls_for_rates(self.base_rates, banner_info)

    def set_base_rates(self, p_type, banner_info):
        self.base_rates = copy.deepcopy(p_type)
        #account for On Banner only and EX rainbow rate
        if banner_info.get('allRainbowsOnBanner') == True:
            for name, pull_rates in self.base_rates.iteritems():
                pull_rates['bannerRainbowRate'] = pull_rates['rainbowRate']
                pull_rates['offBannerRainbowRate'] = 0
        else:
            self.base_rates['guaranteedEXRainbow']['bannerRainbowRate'] = float(banner_info['bannerRainbowCount']) / float(banner_info['fiveStarBaseUnitCount'])
            self.base_rates['guaranteedEXRainbow']['offBannerRainbowRate'] = 1 - self.base_rates['guaranteedEXRainbow']['bannerRainbowRate']
        
