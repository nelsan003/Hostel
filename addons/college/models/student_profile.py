from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StudentProfile(models.Model):
    _name = 'student.profile'
    _inherits = {
        'my.partner': 'partner_id',
    }
    _description = 'Student Profile'

    @api.depends('dob')
    def _get_compute_age(self):
        self.age = 0
        for rec in self:
            if rec.dob:
                curr_year = fields.Date.today().strftime('%Y')
                test = rec.dob.strftime('%Y')
                age = int(curr_year) - int(test)
                rec.age = age



    @api.model
    def default_get(self, fields):
        res = super(StudentProfile, self).default_get(fields)
        res['name'] = 'Enter your name'
        return res

    @api.returns('self')
    def _get_default_code(self):
        return 'Sample code'


    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', default=_get_default_code)
    roll_nb = fields.Char(string='ROll Nb')
    dob = fields.Date(string='Date')
    age = fields.Integer(string='Age', compute='_get_compute_age', store=True)
    department_id = fields.Many2one('student.department', string='Department', required=True)
    language_ids = fields.Many2many('language.info', string='Language', required=True)
    mark_ids = fields.One2many('mark.info', 'student_id', string='Mark')
    image = fields.Image(string='Image')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], default='male')
    programme_id = fields.Many2one('programme.info', string='Programme')
    partner_id = fields.Many2one('my.partner', string='Partner')
    blood_group_id = fields.Many2one('bloodgroup.info')


    @api.onchange('department_id')
    def _onchnage_department(self):
        print('*************************')

    @api.onchange('dob')
    def _onchange_dob(self):
        if self.dob:
            mark_ids = self.mark_ids._origin
            # total = 0
            # for rec in mark_ids:
            #     total += int(rec.mark)
            # print(total)
            test = mark_ids.mapped('name')
            print(test)
            # test = sum([int(rec) for rec in mark_ids.mapped('mark')])
            # print(test)

            # test1 = self.env['mark.info'].sudo().search([
            #     '&',
            #         ('student_id', '=', self.id.origin),
            #     '|',
            #         ('mark', '=', '10'),
            #         ('mark', '=', '20'),
            # ])
            # print(test1)



            # test1 = self.env['mark.info'].sudo().search([
            #     ('student_id', '=', self.id.origin)
            # ], limit=1, order='id desc')
            # print(test1)
            # test = self.env['mark.info'].sudo().search_count([
            #     ('student_id', '=', self.id.origin)
            # ])
            # print(test, '77777777777777777')
            # s_read = self.env['mark.info'].sudo().search_read(
            #     [('student_id', '=', self.id.origin)],
            #     fields=['name', 'student_id']
            # )
            # print(s_read, '****************8')

            # b_id = self.env['mark.info'].sudo().browse(4)
            # print(b_id, 'iiiiiiiiiiiiiiiiiiiiiiiii')
            pass


    def student_send_mail(self):
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&777')


    def redirect_youtube_link(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://www.google.com/',
        }

    # @api.constrains('dob')
    # def vlidate_dob(self):
    #     if self.dob:
    #         curr_year = fields.Date.today().strftime('%Y')
    #         test = self.dob.strftime('%Y')
    #         age = int(curr_year) - int(test)
    #         if not age >= 18:
    #             raise ValidationError('Age should be greater than 18')

    def create(self, values):
        res = super().create(values)

        return res

    @api.ondelete(at_uninstall=False)
    def test_uninstall(self):
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77')

    def write(self, vals):
        result = super(StudentProfile, self).write(vals)
        print(vals, '&&&&&&&&&&&&&&&&&&&&&77777')
        if vals.get('code'):
            mark_ids = self.env['mark.info'].sudo().search([
                ('student_id', '=', self.id),
                ('mark', '=', '10')
            ])
            if mark_ids:
                mark_ids.sudo().write({
                    'name': 'Tamil'
                })
        return result

    def unlink(self):
        mark_ids = self.env['student.leave'].sudo().search([
            ('student_id', '=', self.id)
        ])
        print(mark_ids, '66666666666666666')
        if mark_ids:
            mark_ids.unlink()
        return super().unlink()


    def copy(self, default=None):
        default = {}
        if not default:
            default['code'] = self.code + 'New'
        return super().copy(default=default)








class Department(models.Model):
    _name = 'student.department'
    _description = 'Student Department'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)


class Language(models.Model):
    _name = 'language.info'
    _description = 'Student Department'
    _rec_name = 'l_name'

    l_name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', size=10)


class Programme(models.Model):
    _inherit = 'programme.info'

    type = fields.Selection([
        ('semester', 'Semester'),
        ('anual', 'Anual')
    ], default='semester')


class ResUsers(models.Model):
    _inherit = 'res.users'


    student_id = fields.Many2one('student.profile',string='Student')