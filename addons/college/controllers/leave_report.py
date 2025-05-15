from odoo import http
from odoo.http import request
import io
import datetime
import xlsxwriter

class ReportXlsxController(http.Controller):

    @http.route('/download/xlsx/report/<string:date_from>/<string:date_to>', type='http', auth='user')
    def download_xlsx(self, date_from, date_to, **kwargs):
        output = io.BytesIO()

        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        for rec in range(0, 2):
            sheet = workbook.add_worksheet(f"Student Leave List{rec}")

            header_format = workbook.add_format({
                'bold': True,
                'align': 'center',
                'valign': 'vcenter',
                'bg_color': '#D7E4BC',
                'border': 1
            })

            cell_format = workbook.add_format({
                'align': 'left',
                'valign': 'vcenter',
                'border': 1,
                'text_wrap': True
            })

            sheet.set_column('A:A', 15)
            sheet.set_column('B:B', 25)
            sheet.set_column('C:C', 20)
            sheet.set_column('D:D', 30)

            sheet.write(0, 0, 'S.No', header_format)
            sheet.write(0, 1, 'Student Name', header_format)
            sheet.write(0, 2, 'ROll No', header_format)
            sheet.write(0, 3, 'Reason', header_format)

            leave_ids = request.env['student.leave'].sudo().search([
                ('date', '>=', datetime.datetime.strptime(date_from, '%Y-%m-%d')),
                ('date_to', '<=', datetime.datetime.strptime(date_to, '%Y-%m-%d'))
            ])

            s_no = 1
            row = 1
            for l_id in leave_ids:
                sheet.write(row, 0, s_no, cell_format)
                sheet.write(row, 1, l_id.student_id.name, cell_format)
                sheet.write(row, 2, l_id.student_id.roll_nb, cell_format)
                sheet.write(row, 3, l_id.reason, cell_format )

                s_no += 1
                row += 1

            sheet.merge_range(row, 0, row, 1, 'Student lEVA')

        workbook.close()
        output.seek(0)
        xlsx_data = output.read()

        return request.make_response(
            xlsx_data,
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename="report.xlsx"'),
            ]
        )

    @http.route('/student/leave', type='http', auth='user', methods=['GET'])
    def student_leave_get(self, **kwargs):
        leave_ids = request.env['student.leave'].sudo().search([])
        result = []
        for l_id in leave_ids:
            result.append({
                'student': l_id.student_id.name,
                'id': l_id.id,
                'date_from': l_id.date.strftime('%d-%m-%Y') if l_id.date else '',
                'date_to': l_id.date_to.strftime('%d-%m-%Y') if l_id.date_to else '',
                'reason': l_id.reason
            })
        return request.render("college.student_leave_list", {'data': result})



    @http.route('/student/leave/delete/<int:id>', type='http', auth='user', methods=['GET'])
    def student_leave_delete(self, id, **kwargs):
        if id:
            request.env['student.leave'].sudo().browse(int(id)).unlink()
        return request.render('college.student_leave_success')

    @http.route('/student/leave/form', type='http', auth='user', methods=['GET'])
    def student_leave_get_value(self, **kwargs):
        student_ids = request.env['student.profile'].sudo().search([])
        return request.render(
            'college.student_leave_form_template',
            {'students': student_ids}
        )

    @http.route('/student/leave/submit', type='http', auth='user', website=True, csrf=False, methods=['POST'])
    def student_leave_submit(self, **post):
        student_id = int(post.get('student_id'))
        date_from = post.get('date')
        date_to = post.get('date_to')
        reason = post.get('reason')

        request.env['student.leave'].sudo().create({
            'student_id': student_id,
            'date': date_from,
            'date_to': date_to,
            'reason': reason,
        })
        return request.render('college.student_leave_success')

    @http.route('/student/leave/edit/<int:id>', type='http', auth='user', website=True)
    def student_leave_edit(self, id, **kwargs):
        leave = request.env['student.leave'].sudo().browse(id)
        students = request.env['student.profile'].sudo().search([('id', '=', leave.student_id.id)])
        return request.render(
            'college.student_leave_edit_template',
            {'leave': leave, 'students': students}
        )

    @http.route('/student/leave/update/<int:id>', type='http', auth='user', website=True, csrf=False, methods=['POST'])
    def student_leave_update(self, id, **post):
        leave = request.env['student.leave'].sudo().browse(id)
        leave.write({
            'student_id': int(post.get('student_id')),
            'date': post.get('date'),
            'date_to': post.get('date_to'),
            'reason': post.get('reason'),
        })
        return request.render('college.student_leave_success')




#     frontend

    @http.route('/api/student/leave', type='http', auth='none', methods=['GET'])
    def api_student_leave_get(self, **kwargs):
        leave_ids = request.env['student.leave'].sudo().search([])
        result = []
        for l_id in leave_ids:
            result.append({
                'student': l_id.student_id.name,
                'id': l_id.id,
                'date_from': l_id.date.strftime('%d-%m-%Y') if l_id.date else '',
                'date_to': l_id.date_to.strftime('%d-%m-%Y') if l_id.date_to else '',
                'reason': l_id.reason
            })
        return request.make_json_response(result)

    @http.route('/api/student/leave/delete/<int:id>', type='http', auth='none', methods=['GET'])
    def api_student_leave_delte(self, id, **kwargs):
        print(id, '*********************************8')

    @http.route('/api/student/leave/create', type='json', auth='none', methods=['POST'])
    def api_student_leave_create(self, **kwargs):
        request_data = request.httprequest.get_json()
        print(request_data)







