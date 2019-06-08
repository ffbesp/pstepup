
import os
import json

import sitesettings
import home
import generatehtml


def main():
    template_vars = {
        'title' : 'Banners - ' + sitesettings.SITE_NAME,
        'siteurl' : sitesettings.SITE_URL,
        'sitename' : sitesettings.SITE_NAME,
        'meta_desc' : 'List of step-up banners in Final Fantasy Brave Exvius (FFBE)',
        'last_four_banners' : home.get_last_four_banners('all'),
        'all_banner_info' : home.get_all_banner_info(), 
    }

    bn_path = os.path.join(
        os.getcwd(), os.pardir, os.pardir, os.pardir, 'ffbesp.github.io', 'banner')

    if not os.path.exists(bn_path):
        os.makedirs(bn_path)

    template_file = 'bannerlist.html'
    html_file_loc = os.path.join(bn_path, 'index.html')
    generatehtml.generate_html(
        html_file_loc, template_file, template_vars, os.path.join(os.getcwd(), 'templates'))



if __name__ == '__main__':
    main()