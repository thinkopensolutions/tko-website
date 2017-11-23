# -*- encoding: utf-8 -*-

{
    'name': 'tko_br_website_sale',
    'version': '0.01',
    'category': 'Customizations',
    'sequence': 38,
    'complexity': 'medium',
    'description': ''' This module allows configure orderpoints subtracting quantity on hand of product
''',
    'author': 'ThinkOpen Solutions Brasil',
    'website': 'http://www.tkobr.com',
    'depends': [
        'website_sale',
        'delivery_correios',
        'tko_br_delivery_sale_stock',
    ],
    'data': [
        'views/website_sale_view.xml',
        'views/sale_config_settings_views.xml',
    ],
    'init': [],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,  # If it's True, the modules will be auto-installed when all dependencies are installed
    'certificate': '',
}
