# -*- coding: utf-8 -*-

{
    'name': 'document_format_h7i',
    'summary': """Formatos de documentos h7i""",
    'version': '12.0.1.0.0',
    'description': """Formatos de documentos h7i""",
    'author': 'DDL',
    'company': 'Xtendoo',
    'website': 'http://www.xtendoo.com',
    'category': 'Extra Tools',
    'depends': [
        'base',
        'account',
        'sale',
        'web',
        'stock'
    ],
    'license': 'AGPL-3',
    'data': [
        'views/external_layout_clean.xml',
        'views/report_saleorder_document.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,

}
