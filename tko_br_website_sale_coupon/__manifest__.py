# -*- encoding: utf-8 -*-

{
    'name': 'tko_br_website_sale_coupon',
    'version': '11.0.01',
    'category': 'Customizations',
    'sequence': 38,
    'complexity': 'medium',
    'description': '''  This module makes website_coupon & tko_br_website_sale compatible
''',
    'author': 'ThinkOpen Solutions Brasil',
    'website': 'http://www.tkobr.com',
    'depends': [
        'website_coupon',
        'tko_br_website_sale',
    ],
    'data': [
        'views/templates.xml',
    ],
    'init': [],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,  # If it's True, the modules will be auto-installed when all dependencies are installed
    'certificate': '',
}
