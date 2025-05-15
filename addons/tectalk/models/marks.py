import json
import os
from odoo import models, fields, api
from odoo.exceptions import UserError

class StudentMark(models.Model):
    _name = 'school.student.mark'
    _description = 'Student Marks'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    subject = fields.Char(string='Subject')
    mark = fields.Float(string='Mark')
    max_mark = fields.Float(string='Max Mark')

    @api.model
    def load_marks_from_json(self):
        json_path = os.path.join(
            self.env['ir.config_parameter'].sudo().get_param('school_management.json_path') or '',
            'marks.json'  # Use the correct file name here
        )

        if not os.path.exists(json_path):
            raise UserError(f"JSON file not found at {json_path}")

        with open(json_path, 'r') as f:
            data = json.load(f)

        for student_name, records in data.items():
            student = self.env['school.student'].search([('name', '=', student_name)], limit=1)
            if not student:
                continue

            for entry in records:
                self.create({
                    'student_id': student.id,
                    'subject': entry.get('subject'),
                    'mark': float(entry.get('mark', 0)),
                    'max_mark': float(entry.get('max_mark', 100))
                })
