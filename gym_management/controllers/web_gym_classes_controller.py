from odoo import http
from odoo.http import request

class WebClasses(http.Controller):
    @http.route('/all/classes', website=True, auth='user')
    def index(self, **kw):
        classes = request.env['gym.class'].sudo().search([])
        return request.render('gym_management.classes_template', {'classes': classes})