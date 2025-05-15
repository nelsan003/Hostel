from odoo import fields, models

class Department(models.Model):

    _name = 'department.info'
    _rec_name = 'course'
    _description ='about student information'

    # name = fields.Char(string='Name', required=True)
    course = fields.Char(string='Course')
    #subject = fields.Char(string='Subject')