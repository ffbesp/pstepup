"""Creates HTML page for a stepup banner

Args:
    banner_id (str): lowercase, hyphenated unit names; key from banner_info in appdata

Todo:
    * add equivalent 10+1 probability
    * number of tickets for similar probability
"""

import sys
import os
import json

import appdata
import sitesettings
import stepupbanner
import probabilitycalc
import generatehtml
import nav


UNIT_ICON_BASE_URL = 'https://raw.githubusercontent.com/ffbesp/ffbeEquip/master/static/img/units/'
FLUCTUATING_OFFBANNER_RATES = ['rivera']

def round_for_display(decimal_value):
    """Round a decimal to the thousandths place for web display
    """
    return round(decimal_value * 100, 3)


def combine_rates_and_pulls_for_display(general, banner, oneunit):
    """Create list of pull counts and rates of success for web display

    Returns:
        List of lists with pull count, general rate, banner rate, and single unit rate for each
    """
    combined = []
    sort_by_pull_count = sorted(oneunit, key=lambda k: k, reverse=True)
    oneunit_by_pull = sorted(sort_by_pull_count, key=lambda k: oneunit[k], reverse=True)
    sort_by_pull_count = sorted(banner, key=lambda k: k, reverse=True)
    banner_by_pull = sorted(sort_by_pull_count, key=lambda k: banner[k], reverse=True)
    sort_by_pull_count = sorted(general, key=lambda k: k, reverse=True)
    general_by_pull = sorted(sort_by_pull_count, key=lambda k: general[k], reverse=True)

    for idx, key in enumerate(oneunit_by_pull):
        oneunit_count = oneunit[key]
        banner_key = banner_by_pull[idx] if idx < len(banner_by_pull) else 0
        banner_count = banner.get(banner_key)
        general_key = general_by_pull[idx] if idx < len(general_by_pull) else 0
        general_count = general.get(general_key)

        if oneunit_count == banner_count and oneunit_count == general_count:
            #add all odds if counts are same
            combined.append([
                oneunit_count,
                round_for_display(general_key),
                round_for_display(banner_key),
                round_for_display(key)
            ])
        elif oneunit_count == banner_count and general[1.0] > oneunit_count:
            #if general is different but multiple pulls at 100% exist, display 100% for general
            combined.append(
                [oneunit_count, 100, round_for_display(banner_key), round_for_display(key)])
        elif oneunit_count == banner_count:
            #if general count is different, just do one unit and banner
            combined.append(
                [oneunit_count, None, round_for_display(banner_key), round_for_display(key)])

    return combined


def create_banner_page(banner_id):
    """Creates HTML page for a stepup banner

    Args:
        banner_id (str): lowercase, hyphenated unit names; key from banner_info in appdata
    """
    banner_json = {}
    filename = appdata.banner_info[banner_id]['banner_json']
    with open(os.path.join(os.getcwd(), os.pardir, 'banner', filename), 'r') as banner_file:
        banner_json = json.load(banner_file)

    step_up = stepupbanner.StepUpBanner(appdata.pull_type, banner_json)

    rates_and_pulls, expected_value, at_least_x, summary, exactly_x = {}, {}, {}, {}, {}
    for lap in range(1, step_up.laps + 1):
        r_and_p = {
            type_rate: {rate:pull*lap for rate, pull in rate_pull.items()}
            for type_rate, rate_pull in step_up.rates_and_pulls_per_lap.items()
        }

        exactly_x[lap] = {
            'general' : {
                key:round_for_display(value)
                for key, value in probabilitycalc.get_prob_exactly_x(r_and_p['general']).items()
            },
            'banner' : {
                key:round_for_display(value)
                for key, value in probabilitycalc.get_prob_exactly_x(r_and_p['banner']).items()
            },
            'oneunit' : {
                key:round_for_display(value)
                for key, value in probabilitycalc.get_prob_exactly_x(r_and_p['oneunit']).items()
            }
        }
        at_least_x[lap] = {
            'general' : {
                key:round_for_display(value)
                for key, value in probabilitycalc.get_prob_at_least_x(r_and_p['general']).items()
            },
            'banner' : {
                key:round_for_display(value)
                for key, value in probabilitycalc.get_prob_at_least_x(r_and_p['banner']).items()
            },
            'oneunit' : {
                key:round_for_display(value)
                for key, value in probabilitycalc.get_prob_at_least_x(r_and_p['oneunit']).items()
            }
        }
        summary[lap] = {
            1 : round(at_least_x[lap]['oneunit'][1], 2),
            2 : round(at_least_x[lap]['oneunit'][2], 2),
            4 : round(at_least_x[lap]['oneunit'].get(4, 0.0), 2)
        }
        expected_value[lap] = {
            'general' : round(probabilitycalc.expected_value(r_and_p['general']), 2),
            'banner' :  round(probabilitycalc.expected_value(r_and_p['banner']), 2),
            'oneunit' : round(probabilitycalc.expected_value(r_and_p['oneunit']), 2)
        }
        rates_and_pulls[lap] = (
            combine_rates_and_pulls_for_display(
                r_and_p['general'], r_and_p['banner'], r_and_p['oneunit']))
        if banner_id in FLUCTUATING_OFFBANNER_RATES:
            for rate_list in rates_and_pulls[lap]:
                if rate_list[3] == 100:
                    rate_list[1] = 100
                elif rate_list[3] < 5:
                    rate_list[1] = 5
                elif rate_list[3] >= 5 and rate_list[3] < 7.5:
                    rate_list[1] = 7
                elif rate_list[3] == 7.5:
                    rate_list[1] = 8.75

    unit_icon = (
        UNIT_ICON_BASE_URL + 'unit_icon_'
        + appdata.banner_info[banner_id]['banner_icon'][banner_json['singleUnitDisplayName']]
        + '.png')

    combined_banner_info = appdata.banner_info[banner_id]
    for key, value in banner_json.items():
        if not key == 'steps':
            combined_banner_info[key] = value

    meta_desc = (
        'Expected values and probability for '
        + appdata.banner_info[banner_id]['banner_name'] + ' step-up banner')
    template_vars = {
        'title' : appdata.banner_info[banner_id]['banner_name'] + ' - ' + sitesettings.SITE_NAME,
        'siteurl' : sitesettings.SITE_URL,
        'sitename' : sitesettings.SITE_NAME,
        'meta_desc' : meta_desc,
        'last_four_banners' : nav.get_last_four_banners('all'),
        'banner_info' : combined_banner_info,
        'unit_icon' : unit_icon,
        'one_unit_name' : banner_json['singleUnitDisplayName'],
        'expected_value' : expected_value,
        'rates_and_pulls' : rates_and_pulls,
        'exactly_x' : exactly_x,
        'at_least_x' : at_least_x,
        'summary' : summary
    }

    banner_path = os.path.join(sitesettings.LOCAL_FILE_PATH, 'banner', banner_id)

    if not os.path.exists(banner_path):
        os.makedirs(banner_path)

    template_file = 'banner.html'
    html_file_loc = os.path.join(banner_path, 'index.html')
    generatehtml.generate_html(
        html_file_loc, template_file, template_vars, os.path.join(os.getcwd(), 'templates'))


def main(banner_id):
    """Runs create_banner_page to generate HTML page for stepup banner
    """
    create_banner_page(banner_id)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('ERROR: Specify a banner name to generate HTML file (e.g. "cid")')
    elif sys.argv[1] not in appdata.banner_info:
        print('ERROR: banner not found in appdata:', sys.argv[1])
    else:
        main(sys.argv[1])
