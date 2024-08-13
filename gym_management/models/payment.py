from odoo import fields, models

class Payment(models.Model):
    _name = 'wb.payment'
    _description = 'This is a payment model'

    member_id = fields.Many2one('wb.member', string='Member')
    currency_id = fields.Many2one('res.currency', string='Currency')
    date = fields.Date(string='Payment Date')
    method = fields.Selection([
        ('Cash', 'Cash'),
        ('Card', 'Card')
    ], string='Payment Method')
    membership_type = fields.Many2one('wb.membership', string='Membership Type')
