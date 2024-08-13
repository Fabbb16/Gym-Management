from odoo import http
from odoo.http import request

class WebTrainers(http.Controller):
    @http.route('/all/trainers', website=True, auth='user')
    def index(self, **kw):
        trainers = request.env['wb.trainer'].sudo().search([])
        return request.render('gym_management.trainer_template', {'trainers': trainers})
