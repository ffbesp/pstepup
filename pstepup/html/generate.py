"""Creates HTML pages for project

Default file location is adjacent to this project
"""

import os
import json

import appdata
import banner
import sitesettings
import generatehtml
import nav


def get_all_banner_info():
    """Find banner metadata for all known banners

    Returns:
        List of all banners in reverse chronological order
    """
    all_banner_info = []
    for banner_id, banner_details in appdata.banner_info.items():
        combined_banner_info = banner_details
        combined_banner_info['banner_id'] = banner_id
        #if file exists, grab non-step details
        b_file = os.path.join(os.getcwd(), os.pardir, 'banner', banner_details['banner_json'])
        if os.path.isfile(b_file):
            with open(b_file, 'r') as banner_file:
                banner_json = json.load(banner_file)
            for key, value in banner_json.items():
                if not key == 'steps':
                    combined_banner_info[key] = value
        all_banner_info.append(combined_banner_info)
    return sorted(
        all_banner_info, key=lambda k: k['duration']['start'].replace('-', ''), reverse=True)


def create_about():
    """Creates About HTML page
    """
    meta_desc = (
        'Expected values and probability per lap of step-up banners'
        ' in Final Fantasy Brave Exvius (FFBE)')
    template_vars = {
        'title' : 'About - ' + sitesettings.SITE_NAME,
        'siteurl' : sitesettings.SITE_URL,
        'sitename' : sitesettings.SITE_NAME,
        'meta_desc' : meta_desc,
        'last_four_banners' : nav.get_last_four_banners('all'),
    }

    about_path = os.path.join(sitesettings.LOCAL_FILE_PATH, 'about')

    if not os.path.exists(about_path):
        os.makedirs(about_path)

    template_file = 'about.html'
    html_file_loc = os.path.join(about_path, 'index.html')
    generatehtml.generate_html(
        html_file_loc, template_file, template_vars, os.path.join(os.getcwd(), 'templates'))


def create_banner_list():
    """Creates Banner List HTML page
    """
    template_vars = {
        'title' : 'Banners - ' + sitesettings.SITE_NAME,
        'siteurl' : sitesettings.SITE_URL,
        'sitename' : sitesettings.SITE_NAME,
        'meta_desc' : 'List of step-up banners in Final Fantasy Brave Exvius (FFBE)',
        'last_four_banners' : nav.get_last_four_banners('all'),
        'all_banner_info' : get_all_banner_info(),
    }

    bn_path = os.path.join(sitesettings.LOCAL_FILE_PATH, 'banner')

    if not os.path.exists(bn_path):
        os.makedirs(bn_path)

    template_file = 'bannerlist.html'
    html_file_loc = os.path.join(bn_path, 'index.html')
    generatehtml.generate_html(
        html_file_loc, template_file, template_vars, os.path.join(os.getcwd(), 'templates'))


def create_home():
    """Creates Home HTML page
    """
    meta_desc = (
        'Expected values and probability per lap of step-up'
        ' banners in Final Fantasy Brave Exvius (FFBE)')
    template_vars = {
        'title' : sitesettings.SITE_NAME,
        'siteurl' : sitesettings.SITE_URL,
        'sitename' : sitesettings.SITE_NAME,
        'meta_desc' : meta_desc,
        'last_four_banners' : nav.get_last_four_banners('all'),
        'last_four_single' : nav.get_last_four_banners('single'),
        'last_four_multi' : nav.get_last_four_banners('multi'),
        'all_banner_info' : get_all_banner_info(),
    }

    home_path = os.path.join(sitesettings.LOCAL_FILE_PATH)

    if not os.path.exists(home_path):
        os.makedirs(home_path)

    template_file = 'home.html'
    html_file_loc = os.path.join(home_path, 'index.html')
    generatehtml.generate_html(
        html_file_loc, template_file, template_vars, os.path.join(os.getcwd(), 'templates'))


def main():
    """Generate basic website HTML pages, then pages for all available banners
    """
    create_home()
    create_about()
    create_banner_list()

    for banner_id in appdata.banner_info:
        banner.create_banner_page(banner_id)


if __name__ == '__main__':
    main()
