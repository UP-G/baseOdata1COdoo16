from odoo import models, _, fields
import requests
import logging
from odoo.http import request

_logger = logging.getLogger(__name__)
class Odata1CRoute(models.Model):
    _name = "odata.1c.route"

    route = fields.Char(string='route name', tracking=True)
    url_pattern = fields.Char(string='url pattern', tracking = True)
    connection_id = fields.Many2one("odata.1c.connection", string='connection info')
    
    def get_data(self, pars, obj= None):
        url_part = self.url_pattern.format(**pars)
        return self.connection_id.get_data(url_part, pars, obj)

    #@classmethod 
    def get_by_route(self,route, pars, obj= None):
        return self.search([('route','=',route)]).get_data(pars, obj)

