from odoo import models,fields,api

class ProgrammeInfo(models.Model):
    _name = 'programme.info'
    _description = 'Programme Info'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', size=10)
