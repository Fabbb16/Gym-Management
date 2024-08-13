from odoo import http
from odoo.http import request

class WebSchedule(http.Controller):
    @http.route('/all/schedules', type='http', website=True, auth='user')
    def index(self, **kw):
        # Fetch all schedules
        schedules = request.env['wb.schedule'].sudo().search([])

        # Debugging: Print the number of schedules found
        print(f"Number of schedules found: {len(schedules)}")

        # Render the template with the schedules data
        return request.render('gym_management.schedule_template', {'schedules': schedules})
