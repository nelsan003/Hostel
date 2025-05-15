from odoo import fields, models,api
from odoo.exceptions import ValidationError


class student(models.Model):
    # @api.depends('dob')
    # def _get_compute_age(self):
    #     self.age = 0
    #     for rec in self:
    #         if rec.dob:
    #             curr_year = fields.Date.today().strftime('%Y')
    #             test = rec.dob.strftime('%Y')
    #             age = int(curr_year) - int(test)
    #             rec.age = age

    _name = 'tectalk.student'
    _description ='about student information'

    name = fields.Char(string='Name')
    father_name = fields.Char(string='Father name')
    age= fields.Char(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male')

    dob = fields.Date(string='Dob')
    age = fields.Integer(string='Age')
    department_id =fields.Many2one('department.info',string="Department")
    student_image = fields.Image(string='Upload student image',max_width='100',max_height='100')
    is_department_updated = fields.Boolean(string="Department Updated", default=False)

    mark_ids = fields.One2many('exam.info', 'student_id', string='Mark')

    # @api.constrains('dob')
    # def vlidate_dob(self):
    #     if self.dob:
    #          curr_year = fields.Date.today().strftime('%Y')
    #          test = self.dob.strftime('%Y')
    #          age = int(curr_year) - int(test)
    #        if not age >= 18:
    #             raise ValidationError('Age should be greater than 18')

    @api.onchange('gender')
    def _onchange_gender(self):
        print("nelsan")