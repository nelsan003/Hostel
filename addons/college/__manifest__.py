# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'College',
    'version': '1.2',
    'category': 'College',
    'sequence': 16,
    'summary': 'College',
    'description': """

    """,
    'website': '#',
    'depends': [
        'base',
        'mail',
        'programme'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/cron.xml',
        'data/data.xml',
        'data/leave.xml',
        'data/student_mail_template.xml',
        'views/menu.xml',
        'views/mark.xml',
        'views/student.xml',
        'views/language.xml',
        'views/sequence.xml',
        'views/bloodgroup.xml',

        'wizard/blood_group.xml',
        'wizard/student_leave.xml',
        'wizard/student_sendmail.xml',

        'report/student_leave.xml',
    ],
    'demo': [],
    'css': [],
    'assets': {
        'web.assets_backend': [
            'college/static/src/js/student_profile.js',
            'college/static/src/xml/student_profile.xml',
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
