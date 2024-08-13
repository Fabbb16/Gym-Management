from odoo import fields, models

class GymClass(models.Model):
    _name = 'gym.class'
    _description = 'This is a model of a gym class'

    name = fields.Char(string='Name', help='Name of the class')
    description = fields.Text(string='Description')
    capacity = fields.Integer(string='Capacity')
    trainer_id = fields.Many2one('wb.trainer', string='Trainer')
    member_id = fields.Many2many('wb.member', string='Members')
    equipments_id = fields.Many2many('wb.equipment', string='Equipments')