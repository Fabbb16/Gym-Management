from odoo import fields, models, api

class Members(models.Model):
    _name = 'wb.member'
    _description = 'This is a member model'

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Mobile Phone')
    address = fields.Text(string='Address')
    date_of_birth = fields.Date(string='Date of Birth')
    membership_id = fields.Many2one('wb.membership', string='Membership')
    joining_date = fields.Date(string='Joining Date')
    expiry_date = fields.Date(string='Expiry Date')
    status = fields.Selection([
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    ])
    diet_id = fields.Many2one('wb.diet', string='Diet')

    @api.model
    def create(self, vals):
        # Ensure name and last_name are strings
        name = vals.get('name', '') or ''
        last_name = vals.get('last_name', '') or ''

        partner_vals = {
            'name': name + ' ' + last_name,
            'phone': vals.get('phone'),
            'is_company': False,
            'type': 'contact',
        }
        partner = self.env['res.partner'].create(partner_vals)
        vals['partner_id'] = partner.id
        return super(Members, self).create(vals)




