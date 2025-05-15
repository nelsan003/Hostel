from odoo import http
from odoo.http import request

class StudentMarkController(http.Controller):

    @http.route('/students/mark', type='http', auth='user', methods=['GET'])
    def student_mark_get(self, **kwargs):
        print("hi")
        mark_ids = request.env['exam.info'].sudo().search([])
        result = []
        for l_id in mark_ids:
            result.append({
                'student': l_id.student_id.name,
                'id': l_id.id,
                'subject': l_id.subject,
                'mark': l_id.mark,
            })
        return request.render('tectalk.student_mark_list', {'data': result})

    @http.route('/students/mark/delete/<int:id>', type='http', auth='user', methods=['GET'])
    def student_mark_delete(self, id, **kwargs):
        if id:
            request.env['exam.info'].sudo().browse(int(id)).unlink()
        return request.render('tectalk.student_mark_success')

    @http.route('/students/mark/form', type='http', auth='user', methods=['GET'])
    def student_mark_get_value(self, **kwargs):
        student_ids = request.env['tectalk.student'].sudo().search([])
        return request.render(
            'tectalk.student_mark_form_template',
            {'students': student_ids}
        )

    @http.route('/students/mark/submit', type='http', auth='user', website=True, csrf=False, methods=['POST'])
    def student_mark_submit(self, **post):
        student_id = int(post.get('student_id'))
        subject = post.get('subject')
        mark = post.get('mark')

        # Validate mark
        try:
            mark_val = float(mark)
            if mark_val < 0 or mark_val > 100:
                raise ValueError()
        except ValueError:
            student_ids = request.env['tectalk.student'].sudo().search([])
            return request.render('tectalk.student_mark_form_template', {
                'students': student_ids,
                'error': "Invalid mark. Please enter a number between 0 and 100.",
                'old_data': {
                    'student_id': student_id,
                    'subject': subject,
                    'mark': mark,
                }
            })

        # If valid, create record
        request.env['exam.info'].sudo().create({
            'student_id': student_id,
            'subject': subject,
            'mark': mark,
        })
        return request.render('tectalk.student_mark_success')

    @http.route('/students/mark/edit/<int:id>', type='http', auth='user', website=True)
    def student_mark_edit(self, id, **kwargs):
        mark = request.env['exam.info'].sudo().browse(id)
        students = request.env['tectalk.student'].sudo().search([('id', '=', mark.student_id.id)])
        return request.render(
            'tectalk.student_mark_edit_template',
            {'mark': mark, 'students': students}
        )

    @http.route('/students/mark/update/<int:id>', type='http', auth='user', website=True, csrf=False, methods=['POST'])
    def student_mark_update(self, id, **post):
        mark = request.env['exam.info'].sudo().browse(id)
        mark.write({
            'student_id': int(post.get('student_id')),
            'subject': post.get('subject'),
            'mark': post.get('mark'),
        })
        return request.render('tectalk.student_mark_success')

    #     frontend

    @http.route('/api/students/mark', type='http', auth='none', methods=['GET'])
    def api_student_mark_get(self, **kwargs):
        mark_ids = request.env['exam.info'].sudo().search([])
        result = []
        for l_id in mark_ids:
            result.append({
                'student': l_id.student_id.name,
                'id': l_id.id,
                'subject': l_id.subject,
                'mark': l_id.mark,
            })
        return request.make_json_response(result)

    @http.route('/api/students/mark/delete/<int:id>', type='http', auth='none', methods=['GET'])
    def api_student_mark_delte(self, id, **kwargs):
        print(id, '*********************************8')

    @http.route('/api/students/mark/create', type='json', auth='none', methods=['POST'])
    def api_student_mark_create(self, **kwargs):
        request_data = request.httprequest.get_json()
        print(request_data)