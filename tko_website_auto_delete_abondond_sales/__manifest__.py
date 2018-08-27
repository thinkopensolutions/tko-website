# -*- coding: utf-8 -*-
# Copyright 2017 Jairo Llopis <jairo.llopis@tecnativa.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Auto delete abondend sales",
    "summary":"Auto vacuum abondened website sales",
    "description": "Website creates draft quotations with public user, even before someone logs in to the system"
               "Even buyer doesn't continue buying process he leaves an abondened sale in system with Customer as Public user"
               "This module will delete those sales after no of hours set in system parameter 'tko_website_auto_delete_abondond_sales'",
    "version": "10.0.1.0.1",
    "category": "Extra Tools",
    "website": "https://www.tko-br.com/",
    "author": "TKO, Odoo S.A., Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "website_sale",
    ],
    "data": [
        'views/abondoned_sales_scheduler_view.xml',
        'data/ir_config_parameter_view.xml',
    ],
    "qweb": [
    ],
}
