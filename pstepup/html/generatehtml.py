#!/usr/bin/env python
"""Generate static HTML files

Usage:
    import generatehtml

    generatehtml.generate_html('/path/to/file', 'template.html', dict_of_variables, '/path/to/templates')
"""
import io

import jinja2


def get_page_template(template_file, search_path):
    template_loader = jinja2.FileSystemLoader( searchpath=search_path )
    template_env = jinja2.Environment( loader=template_loader, trim_blocks=True, lstrip_blocks=True )
    return template_env.get_template(template_file)


def generate_html(file_loc, template_file, template_vars, search_path):
    template = get_page_template(template_file, search_path)
    with io.open(file_loc, 'w', encoding='utf-8') as html_file:
        html_file.write(template.render(template_vars))
    print(file_loc, 'write successful')