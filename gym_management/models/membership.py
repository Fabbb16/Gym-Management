from odoo import fields, models

class Membership(models.Model):
    _name = 'wb.membership'
    _description = 'This is a membership model'

    name = fields.Char(string='Name', help='membership type')
    description = fields.Text(string='Description')
    currency_id = fields.Many2one('res.currency', string='Currency')
    price = fields.Float(string='Float')
    duration = fields.Selection([
        ('1 month', '1 month'),
        ('3 months', '3 months'),
        ('6 months', '6 months'),
        ('1 year', '1 year')
    ])