# -*- coding: utf-8 -*-
{
    'name': "Train Transportation",

    'summary': "Modul Train Transportation",

    'description': """
Modul Train Transportation untuk Study Case Juke Solutions
    """,

    'author': "Aldiriansyah Dwi Febrianto",
    'website': "https://www.jukesolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/train_views.xml',
        'views/menuitem_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

