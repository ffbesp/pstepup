
import os

import sitesettings
import generatehtml
import home


def main():
    template_vars = { 'title' : 'About - ' + sitesettings.SITE_NAME,
                    'siteurl' : sitesettings.SITE_URL,
                    'sitename' : sitesettings.SITE_NAME,
                    'meta_desc' : 'Expected values and probability per lap of step-up banners in Final Fantasy Brave Exvius (FFBE)',
                    'last_four_banners' : home.get_last_four_banners('all'), }

    if not os.path.exists(os.path.join(os.getcwd(), os.pardir, os.pardir, os.pardir, 'ffbesp.github.io', 'about')):
        os.makedirs(os.path.join(os.getcwd(), os.pardir, os.pardir, os.pardir, 'ffbesp.github.io', 'about'))

    template_file = 'about.html'
    html_file_loc = os.path.join(os.getcwd(), os.pardir, os.pardir, os.pardir, 'ffbesp.github.io', 'about', 'index.html')
    generatehtml.generate_html(html_file_loc, template_file, template_vars, os.path.join(os.getcwd(), 'templates'))



if __name__ == '__main__':
    main()