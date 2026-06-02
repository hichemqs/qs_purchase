{
    'name': "QS Purchase",

    'version': "19.0.1.0.0",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',

    # any module necessary for this one to work correctly
    'depends': [
        'purchase',
        'mrp',
        'sale',
        'project',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_gantt_view.xml',
        'views/purchase_search_view.xml',
        'views/purchase_action_inherit.xml',
        'views/as_planning_action.xml',
        'views/as_planning_gantt_view.xml',
        'views/mrp_menu.xml',
        'views/mrp_search_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

