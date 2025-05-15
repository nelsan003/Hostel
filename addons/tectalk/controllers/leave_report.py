from odoo import http
from odoo.http import request
import io
import datetime
import xlsxwriter


class StudentLeaveController(http.Controller):

    @http.route('/students/leave', type='http', auth='user', methods=['GET'])
    def student_leave_get(self, **kwargs):
        leave_ids = request.env['attendence.info'].sudo().search([])
        result = []
        for l_id in leave_ids:
            result.append({
                'student': l_id.student_id.name,
                'id': l_id.id,
                'date_from': l_id.date.strftime('%d-%m-%Y') if l_id.date else '',
                'date_to': l_id.date_to.strftime('%d-%m-%Y') if l_id.date_to else '',
                'reason': l_id.reason
            })
        return request.render("tectalk.student_leave_list", {'data': result})

    @http.route('/students/leave/delete/<int:id>', type='http', auth='user', methods=['GET'])
    def student_leave_delete(self, id, **kwargs):
        if id:
            request.env['attendence.info'].sudo().browse(int(id)).unlink()
        return request.render('tectalk.student_leave_success')
