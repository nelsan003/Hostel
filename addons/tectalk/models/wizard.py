from odoo import models, fields,api,_

class MySimpleWizard(models.TransientModel):
    _name = 'my.simple.wizard'
    _description = 'Simple Wizard '

    name = fields.Char(string="Name")
    student_id = fields.Many2one('tectalk.student', string='Student', ondelete='cascade')
    department_ids = fields.Many2many('department.info', string="Department")
    student_ids = fields.One2many('student.department.update.wizard','trans_id')
    def action_confirm(self):
        self.env['tectalk.student'].browse(self._context.get('active_ids')).write({'name':self.name,'student_id':self.student_id})
        print(f"User entered: {self.name}")
        for line in self.student_ids:
            if line.student_id:
                line.student_id.department_id = line.department_id.id
                line.student_id.is_department_updated = True

    @api.onchange('department_ids')
    def _onchange_department_methods(self):
        self.student_ids = False
        data = []
        print(self.department_ids)
        for rec in self.department_ids:
            student_ids = self.env['tectalk.student'].sudo().search([
                ('department_id', '=', rec._origin.id),
                ('is_department_updated', '=', False)
            ])
            for student_id in student_ids:
                data.append((0, 0, {
                    'student_id': student_id.id,
                    'department_id': rec._origin.id,
                }))
        print(data)
        self.student_ids = data


class TechTalkStudentDept(models.TransientModel):
    _name = 'student.department.update.wizard'


    student_id = fields.Many2one('tectalk.student',string="Student")
    department_id = fields.Many2one('department.info', string="Department")
    trans_id = fields.Many2one('my.simple.wizard')