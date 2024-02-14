# -*- coding: utf-8 -*-
{
    'name' : 'Lead Stages',
    'version' : '17.0.0.0.0',
    'summary': 'Lead Stages',
    'category': 'crm',
    'depends': ['base','crm'],
    'data': [
        'data/lead_stages_data.xml',
        'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
        'views/crm_lead_stages.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
# Part of Odoo. See LICENSE file for full copyright and licensing details.
