from odoo import models, fields
from odoo.exceptions import ValidationError


class BloodGroupUpdateWizard(models.TransientModel):
    _name = 'blood.group.update'
    _description = 'Blood Group Update'


    blood_group_id = fields.Many2one('bloodgroup.info', string='Blood Group')
    student_ids = fields.One2many('student.list.update', 'wizard_id')


    def udpate_blood_group(self):
        if not self.student_ids:
            raise ValidationError('Data not found')

        for rec in self.student_ids:
            rec.student_id.sudo().write({
                'blood_group_id': self.blood_group_id.id,
                'uid': rec.phone_number
            })

        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Blood Group updated succesfully ',
                'type': 'rainbow_man',
            }
        }


class StudentList(models.TransientModel):
    _name = 'student.list.update'

    wizard_id = fields.Many2one('blood.group.update', string='Student')
    student_id = fields.Many2one('student.profile', string='Student')
    phone_number = fields.Char(string='Phone NO', related='student_id.uid')


