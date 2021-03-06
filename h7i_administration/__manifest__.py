{
    'name': 'H7I Administration',
    'summary': """Administration settings for Hierros 7 Islas""",
    'version': '12.0.1.0.0',
    'description': """Administration settings for h7i""",
    'author': 'Dani Domínguez',
    'company': 'Xtendoo',
    'website': 'http://xtendoo.es',
    'category': 'Admin Tools',
    'depends': [
        'base',
        'sale',
        'product',
    ],
    'license': 'AGPL-3',
    'data': [
        'views/sale_order_views.xml',
        'security/security_group.xml'
    ],
    'installable': True,
    'auto_install': True,
}
