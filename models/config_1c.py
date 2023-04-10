from odoo import api, fields, models, _
from odoo.addons.base_odata_1c.models.user_1c import Catalog, Infobase

class ConfigOneC(models.Model):
    _name = "config.1c"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    login = fields.Char(string='Login', tracking=True)
    password = fields.Char(string='Password', tracking=True)
    url = fields.Char(string='Url', tracking=True)
    infobase = fields.Char(string='Infobase', tracking=True)

    def get_users(self):
        connection = Infobase(self.url, self.infobase, self.login, self.password)
        users = Catalog(connection, 'Пользователи')
        data = users.query(select='Description')
        for jsonDATA in data:
            if not self.env['user.1c'].search([('description', '=', jsonDATA['Description'])])['description']:
                self.env['user.1c'].create({
                    'description': jsonDATA['Description']
                })
        return



