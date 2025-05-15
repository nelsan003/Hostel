from odoo import models, fields, api

class StudentLeaveReport(models.AbstractModel):
    _name = 'report.college.report_student_leave'
    _description = 'Employee Resume'

    @api.model
    def _get_report_values(self, docids, data=None):
        context = data['context']
        docs = self.env[context['active_model']].sudo().browse(context['active_id'])
        leave_ids = self.env['student.leave'].sudo().search([
            ('date', '>=', docs.date_from),
            ('date_to', '<=', docs.date_to)
        ])
        return {
            'doc_ids': docids,
            'result': leave_ids,
            'docs': docs
        }
from odoo import models, fields, api

class StudentLeaveReport(models.AbstractModel):
    _name = 'report.tectalk.report_student_leave'
    _description = 'Student Data'

    @api.model
    def _get_report_values(self,docids, data=None):
        context = data['context']
        docs = self.env[context['active_model']].sudo().browse(context['active_id'])
        leave_ids = self.env['attendence.info'].sudo().search([
            ('')

        ])