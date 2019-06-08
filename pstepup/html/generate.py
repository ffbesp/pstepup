"""Creates HTML pages for project

Default file location is adjacent to this project; from this
location: ../../../ffbesp.github.io/
"""

import os

import appdata
import home
import banner
import sitesettings
import generatehtml


def create_about():
    """Creates About HTML page on file system at ../../../ffbesp.github.io/about/index.html
    """
    meta_desc = ('Expected values and probability per lap of step-up banners'
        ' in Final Fantasy Brave Exvius (FFBE)')
    template_vars = {
        'title' : 'About - ' + sitesettings.SITE_NAME,
        'siteurl' : sitesettings.SITE_URL,
        'sitename' : sitesettings.SITE_NAME,
        'meta_desc' : meta_desc,
        'last_four_banners' : home.get_last_four_banners('all'),
    }

    about_path = os.path.join(
        os.getcwd(), os.pardir, os.pardir, os.pardir, 'ffbesp.github.io', 'about')

    if not os.path.exists(about_path):
        os.makedirs(about_path)

    template_file = 'about.html'
    html_file_loc = os.path.join(about_path, 'index.html')
    generatehtml.generate_html(
        html_file_loc, template_file, template_vars, os.path.join(os.getcwd(), 'templates'))


def create_banner_list():
    """Creates Banner List HTML page on file system at ../../../ffbesp.github.io/banner/index.html
    """
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


def main():
    home.main()
    create_about()
    create_banner_list()

    for banner_id in appdata.banner_info:
        banner.create_banner_page(banner_id)


if __name__ == '__main__':
    main()