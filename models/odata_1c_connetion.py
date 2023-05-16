from odoo import api, fields, models, _
import requests
import json
import logging
#from odoo.addons.base_odata_1c.models.user_1c import Catalog, Infobase

_logger = logging.getLogger(__name__)
class Odata1CConnection(models.Model):
    _name = "odata.1c.connection"

    login = fields.Char(string='Login', tracking=True)
    password = fields.Char(string='Password', tracking=True)
    url_pattern = fields.Char(string='Url', tracking=True)

    def get_data(self, url_part, pars, obj= None):
        url = self.url_pattern.format(url_part=url_part)
        auth = requests.auth.HTTPBasicAuth(self.login, self.password)
        _logger.info(url)
        return json.loads(requests.get(url, auth=auth).content)
        

