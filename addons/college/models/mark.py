from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MarkInfo(models.Model):
    _name = 'mark.info'

    sequence = fields.Integer(default=1)
    name = fields.Char(string='Subject Name', required=True)
    mark = fields.Char(string='Mark', required=True)
    student_id = fields.Many2one('student.profile', string='Student', ondelete='set null')
    stu_name = fields.Char(srting='Stu Name', related='student_id.name',)
    states = fields.Selection([
        ('draft', 'Draft'),
        ('approve', 'Approve'),
        ('reject', 'Reject')
    ], default='draft')


    def approve_mark(self):
        self.sudo().write({'states': 'approve'})

    def reject_mark(self):
        self.states = 'reject'



    @api.onchange('mark')
    def _onchange_date__(self):
        stu_ids = self.env['student.profile'].sudo().search([])
        for rec in stu_ids.sorted(lambda l: l.name or ''):
            print(rec.name)
        # male_count = stu_ids.filtered(
        #     lambda l: l.gender == 'male'
        #     and l.age == 25
        # )
        # female_count = stu_ids.filtered(lambda l:l.gender == 'female')
        # print(male_count)
        # print(female_count)


    # @api.constrains('student_id')
    # def validate_dupilcate(self):
    #     if self.student_id:
    #         for rec in self:
    #             rec_ids = self.sudo().search([
    #                 ('student_id', '=', rec.student_id.id),
    #             ])
    #             if len(rec_ids) > 1:
    #                 raise ValidationError('Duplicate record found !!')



class StudentLeave(models.Model):
    _name = 'student.leave'


    student_id = fields.Many2one('student.profile', string='Student', required=True)
    date = fields.Date(string='Date')
    reason = fields.Char(String='Reason')

    #
    date_to = fields.Date(string='Date To')
    duration = fields.Float()
    color = fields.Char()



