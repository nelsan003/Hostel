from odoo import fields, models

class Bloodgroup(models.Model):

    _name = 'bloodgroup.info'
    _description ='about bloodgroup information'

    name = fields.Char(string='Name', required=True)
    group = fields.Char(string='Group')
    #subject = fields.Char(string='Subject')