from odoo import fields, models

class Reception(models.Model):
    _name = 'wb.rec'
    _description = 'This is a receptionist model'

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('Female', 'Female'),
        ('Male', 'Male')
    ])
    phone = fields.Char(string='phone')
    api_key = fields.Char(string='Key')