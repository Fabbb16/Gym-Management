from odoo import fields, models

class Equipments(models.Model):
    _name = 'wb.equipment'
    _description = 'This is an equipment model'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')