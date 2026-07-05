import json, datetime, pytz
from odoo import fields, models, http, _
from odoo.http import request

class controller_website(http.Controller):
                
    @http.route('/aboutus', type='http', auth='public', website=True)
    def portal_aboutus(self):
        return request.render("instance_solesgps.website_aboutus")
