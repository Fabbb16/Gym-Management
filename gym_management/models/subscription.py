from odoo import fields, models

class Subscription(models.Model):
    _name = 'wb.subscription'
    _description = 'This is a subscription model'

    member_id = fields.Many2one('wb.member', string='Member')
    membership_id = fields.Many2one('wb.membership', string='Membership')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    status = fields.Selection([
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    ])