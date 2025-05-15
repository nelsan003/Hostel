# from odoo import models, fields, api
# from odoo.exceptions import ValidationError
#
#
# class Exam(models.Model):
#
#     _name = 'exam.info'
#     _description ='about student information'
#
#     subject = fields.Char(string='Subject')
#     mark = fields.Char(string='Mark')
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Exam(models.Model):
    _name = 'exam.info'
    _description = 'About student exam information'

    student_id = fields.Many2one('tectalk.student', string='Student', required=True ,ondelete='cascade')
    subject = fields.Char(string='Subject', required=True)
    mark = fields.Float(string='Mark')

    @api.constrains('student_id')
    def _check_subject_limit(self):
        for record in self:
            subject_count = self.search_count([
                ('student_id', '=', record.student_id.id)
            ])
            if subject_count > 5:
                raise ValidationError("A student cannot have more than 5 subjects.")

    @api.constrains('mark')
    def _check_mark_limit(self):
        for record in self:
            if record.mark > 100:
                raise ValidationError("Mark cannot be greater than 100.")
            if record.mark < 0:
                raise ValidationError("Mark cannot be less than 0.")

    @api.onchange('student_id')
    def _onchange_student_id(self):
        for record in self:
            if record.student_id:
                exam_records = self.search([('student_id', '=', record.student_id.id)])
                subject_list = [rec.subject for rec in exam_records]
                total_marks = sum(rec.mark for rec in exam_records)
                max_marks = len(subject_list) * 100

                summary = {
                    "Student Name": record.student_id.name,
                    "Subjects": subject_list,
                    "Maximum Marks": max_marks,
                    "Marks Obtained": total_marks
                }

                print("Student Exam Summary :", summary)
