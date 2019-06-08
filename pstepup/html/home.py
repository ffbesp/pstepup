
import os
import json

import appdata
import sitesettings
import generatehtml


def get_last_four_banners(banner_type):
    banner_list = []
    for banner_id, banner_details in appdata.banner_info.items():
        combined_banner_info = banner_details
        combined_banner_info['banner_id'] = banner_id
        banner_list.append(combined_banner_info)

    if banner_type == 'all':
        return sorted(banner_list, key=lambda k: k['duration']['start'].replace('-',''), reverse=True)[:4]
    elif banner_type == 'single':
        return sorted([x for x in banner_list if len(x['banner_icon']) == 1], key=lambda k: k['duration']['start'].replace('-',''), reverse=True)[:4]
    elif banner_type == 'multi':
        return sorted([x for x in banner_list if len(x['banner_icon']) > 1], key=lambda k: k['duration']['start'].replace('-',''), reverse=True)[:4]


def get_all_banner_info():
    all_banner_info = []
    for banner_id, banner_details in appdata.banner_info.items():
        combined_banner_info = banner_details
        combined_banner_info['banner_id'] = banner_id
        #if file exists, grab non-step details
        if os.path.isfile(os.path.join(os.getcwd(), os.pardir, 'banner', banner_details['banner_json'])):
            with open(os.path.join(os.getcwd(), os.pardir, 'banner', banner_details['banner_json']), 'r') as banner_file:
                banner_json = json.load(banner_file)
            for key, value in banner_json.items():
                if not key == 'steps':
                    combined_banner_info[key] = value
        all_banner_info.append(combined_banner_info)
    return sorted(all_banner_info, key=lambda k: k['duration']['start'].replace('-',''), reverse=True)


def main():
    meta_desc = ('Expected values and probability per lap of step-up'
        ' banners in Final Fantasy Brave Exvius (FFBE)')
    template_vars = {
        'title' : sitesettings.SITE_NAME,
        'siteurl' : sitesettings.SITE_URL,
        'sitename' : sitesettings.SITE_NAME,
        'meta_desc' : meta_desc,
        'last_four_banners' : get_last_four_banners('all'),
        'last_four_single' : get_last_four_banners('single'),
        'last_four_multi' : get_last_four_banners('multi'),
        'all_banner_info' : get_all_banner_info(),
    }

    home_path = os.path.join(os.getcwd(), os.pardir, os.pardir, os.pardir, 'ffbesp.github.io')

    template_file = 'home.html'
    html_file_loc = os.path.join(home_path, 'index.html')
    generatehtml.generate_html(
        html_file_loc, template_file, template_vars, os.path.join(os.getcwd(), 'templates'))



if __name__ == '__main__':
    main()