from odoo import api, fields, models, _

import requests
import json

class UserOneC(models.Model):
    _name = "user.1c"
    _description = "Odata 1C User"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    description = fields.Char(string='Description')
    user_id_ib = fields.Char(string='UserIdIB')
    not_valid = fields.Boolean(string='Not valid')

class Infobase:
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Connection': 'keep-alive'
    }

    def __init__(self, server, infobase, username, password):
        self.server = server
        self.infobase = infobase
        self.full_url = server + infobase + \
                         '/odata/standard.odata/{obj}?$format=json'
        self.auth = requests.auth.HTTPBasicAuth(username, password)


def make_url_part(name, value, value_type):
    if value is None:
        return ''
    if type(value) != value_type:
        raise ValueError('{}={} must be {}'.format(
            name, value, value_type))
    result = "&${}={}".format(name, value)
    return result


class Catalog:
    infobase: Infobase

    def __init__(self, infobase, catname):
        self.infobase = infobase
        self.catname = catname
        self.url = self.infobase.full_url.format(obj='Catalog_'+self.catname)

    def get(self, guid, select=None):
        obj = "Catalog_{}(guid'{}')".format(self.catname, guid)
        url = self.infobase.full_url.format(obj=obj)
        _url_select = make_url_part('select', select, str)
        url = url + _url_select
        result = requests.get(url, auth=self.infobase.auth,
                         headers=self.infobase.headers)
        if result.status_code != 200:
            raise Exception(result.text)
        return json.loads(result.text)

    def query(self, select=None):
        _url_select = make_url_part('select', select, str)
        url = self.url + _url_select
        result = requests.get(url, auth=self.infobase.auth,
                         headers=self.infobase.headers)
        if result.status_code != 200:
            raise Exception(result.text)
        return json.loads(result.text)['value']