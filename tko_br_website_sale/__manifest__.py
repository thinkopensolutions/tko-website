# -*- encoding: utf-8 -*-

{
    'name': 'tko_br_website_sale',
    'version': '11.0.01',
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
        'website_sale_delivery',
        'tko_br_delivery_sale_stock',
    ],
    'data': [
        'static/src/xml/website_sale_view.xml',
        'views/website_sale_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'init': [],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,  # If it's True, the modules will be auto-installed when all dependencies are installed
    'certificate': '',
}
