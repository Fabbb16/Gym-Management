# -*- coding: utf-8 -*-
{
    'name': "gym_management",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'installable': True,
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/member_views.xml',
        'views/trainer_views.xml',
        'views/membership_views.xml',
        'views/gym_class_views.xml',
        'views/equipment_views.xml',
        'views/schedule_views.xml',
        'views/subscription_views.xml',
        'views/payment_views.xml',
        'views/reception_views.xml',
        'views/diet_views.xml',
        'views/web_trainer_template.xml',
        'views/web_classes_template.xml',
        'views/web_schedule_template.xml'
    ]
}

