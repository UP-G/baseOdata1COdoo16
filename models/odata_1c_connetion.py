from odoo import api, fields, models, _
import requests
import json
import logging
#from odoo.addons.base_odata_1c.models.user_1c import Catalog, Infobase

_logger = logging.getLogger(__name__)
class Odata1CConnection(models.Model):
    _name = "odata.1c.connection"
    _description = "Odata 1C connection"
    
    name = fields.Char(string='Name connection')
    login = fields.Char(string='Login')
    password = fields.Char(string='Password')
    url_pattern = fields.Char(string='Url')

    def get_data(self, url_part, pars, obj= None):
        url = self.url_pattern.format(url_part=url_part)
        auth = requests.auth.HTTPBasicAuth(self.login, self.password)
        _logger.info(url)
        return json.loads(requests.get(url, auth=auth).content)
        

