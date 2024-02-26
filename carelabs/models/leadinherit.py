from odoo import models, fields

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    x_contact_medium = fields.Char(string="Contact Medium")

    service = fields.Many2many(
        'product.product', string='Services',
        help='Select services related to this lead.'
    
    )