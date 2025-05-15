from odoo import models, fields, api
from odoo.exceptions import UserError



class Attendence(models.Model):
    _name = 'attendence.info'
    _description = 'about student information'

    student_id = fields.Many2one('tectalk.student', string='Student', required=True)
    date = fields.Date(string="Start Date")
    date_to = fields.Date(string="End Date")
    reason = fields.Text()
    duration = fields.Float(string="Duration")
    color = fields.Char(string="Color")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft')

    def action_approve(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError("Only draft records can be approved.")
            rec.state = 'approved'

    def action_reject(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError("Only draft records can be rejected.")
            rec.state = 'rejected'

    def action_reset(self):
        for rec in self:
            if rec.state not in ['approved', 'rejected']:
                raise UserError("Only approved or rejected records can be reset.")
            rec.state = 'draft'
