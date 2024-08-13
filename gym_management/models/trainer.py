from odoo import fields, models

class Trainer(models.Model):
    _name = 'wb.trainer'
    _description = 'This is a trainer model'

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Mobile Phone')
    specialization = fields.Text(string='Specialization')
    notes = fields.Text(string='Experience')
    api_key = fields.Char(string='Key')
