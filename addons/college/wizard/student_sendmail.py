from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StudentSendmail(models.TransientModel):
    _name = 'student.send.mail'

    student_ids  = fields.Many2many('student.profile',string="Students")

    def action_send_emails(self):
        template = self.env.ref('college.student_email_template')
        for student in self.student_ids:
            if student.roll_nb:
                template.with_context(lang='en_US').send_mail(student.id, force_send=True)