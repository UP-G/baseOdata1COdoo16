{
    'name': '1C_base_odata',
    'category': 'Technical',
    'depends': [
        'base',
        'web',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/user_1c_view.xml',
        'views/config_1c_view.xml',
        'views/odata_1c_menu_views.xml',
    ],
    'installable': True,
    'application': True,
}