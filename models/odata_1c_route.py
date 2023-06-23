from odoo import models, _, fields
import requests
import logging
from odoo.http import request

_logger = logging.getLogger(__name__)
class Odata1CRoute(models.Model):
    _name = "odata.1c.route"
    _description = "Odata 1C route"

    route = fields.Char(string='route name')
    url_pattern = fields.Char(string='url pattern')
    description = fields.Text(string='description')
    connection_id = fields.Many2one("odata.1c.connection", string='connection info')
    
    def get_data(self, pars, obj= None):
        
        pars = {k:v for k,v in pars.items() if self.url_pattern.find("{"+k+"}")!=-1}
        if pars == {}:
            return False
        url_part = self.url_pattern.format(**pars)
        return self.connection_id.get_data(url_part, pars, obj)

    def get_by_route(self,route, pars, obj= None):
        _logger.info(self.search([('route','=',route)]))
        return self.search([('route','=',route)]).get_data(pars, obj)

