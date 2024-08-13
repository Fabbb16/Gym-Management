from odoo import fields, models

class Diet(models.Model):
    _name = 'wb.diet'
    _description = 'This is a diet model'

    name = fields.Char(string='Diet', help='Name of the diet')
    trainer_id = fields.Many2one('wb.trainer',string='Trainer')
    diet_menu = fields.Text(string='Diet Menu')