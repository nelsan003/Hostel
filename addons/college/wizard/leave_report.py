from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentLeaveReport(models.TransientModel):
    _name = 'student.leave.report'
    _description = 'Student leave Report'

    date_from = fields.Date(string='Date From', required=True)
    date_to = fields.Date(string='Date To', required=True)


    @api.constrains('date_from', 'date_to')
    def validate_date(self):
        if self.date_from > self.date_to:
            raise ValidationError('Date to must be greater than date from')


    def print_pdf(self):
        return self.env.ref('college.action_student_leave_report').report_action(
            self,
            data= {
                'date_from': self.date_from,
                'date_to': self.date_to
            }
        )


    def print_xlsx(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': f'/download/xlsx/report/{self.date_from}/{self.date_to}',
        }


