from odoo import models, fields, api

class MyPartner(models.Model):
    _name = 'my.partner'

    uid = fields.Char(string='Aadhar', size=12, required=True)


    def test(self):
        print('********************8888')


class MySequence(models.Model):
    _name = 'my.sequence'
    _inherits = {
        'ir.sequence': 'sequence_id',
    }

    sequence_id = fields.Many2one("ir.sequence", string='Main Sequence', required=True, ondelete='cascade')