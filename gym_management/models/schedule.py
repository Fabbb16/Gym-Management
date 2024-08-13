from odoo import fields, models

class Schedule(models.Model):
    _name = 'wb.schedule'
    _description = 'This is a schedule model'

    class_id = fields.Many2one('gym.class', string='Class')
    trainer_id = fields.Many2one('wb.trainer', string='Trainer')
    location = fields.Char(string='Location')
    start_time = fields.Float(string='Time', help='This is the start time of this class. --> 15.30 = 15:30')