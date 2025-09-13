{
    'name': 'Legal Case Management',
    'version': '18.0.1.0.0',
    'category': 'Legal',
    'summary': 'Manage legal cases and hearings',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/legal_views.xml',
        'views/legal_menus.xml',
    ],
    'installable': True,
    'application': True,
}
