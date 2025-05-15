# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Programme',
    'version': '1.2',
    'category': 'College',
    'sequence': 16,
    'summary': 'Programme',
    'description': """

    """,
    'website': '#',
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
