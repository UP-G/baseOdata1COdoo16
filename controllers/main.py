import json
import logging
from odoo import http
from odoo.http import request

from odoo.addons.base_odata_1c.models.odata_1c_route import Odata1CRoute

_logger = logging.getLogger(__name__)

class OneCController(http.Controller):
    
    @http.route('/odata_1c/1c_ut/call_report/', type='http', auth='public', methods=['POST'], csrf=False) 
    def call(self, **args):
        value = http.request.env['odata.1c.route'].get_by_route("1c_ut/debts/", request.get_json_data())
        # _logger.info(value[0])
        return http.request.render("base_odata_1c.debts_template", {"documents": value})

    @http.route(['/odata_1c/<string:base_name>/<string:route_name>/',
                 '/odata_1c/<string:route_name>/'], type='json', auth='public', methods=['POST'], csrf=False) 
    def get_data(self,route_name=None,base_name="1c_ut", **args):
        return http.request.env['odata.1c.route'].get_by_route(f"{base_name}/{route_name}/", request.get_json_data())
    
    # @http.route('/odata_1c/debts_avg/', type='json', auth='public', methods=['POST'], csrf=False) 
    # def get_debts_avg(self, **args):
    #     return http.request.env['odata.1c.route'].get_by_route('1c_ut/debts_avg', {'client_id': request.get_json_data().get('client_id')})

    # @http.route('/odata_1c/debts2/', type='json', auth='public', methods=['POST'], csrf=False) 
    # def get_debts2(self, client_id, **args):
    #     return http.request.env['odata.1c.route'].get_by_route('1c_ut/debts', client_id)

    # @http.route('/odata_1c/debts_avg2/', type='json', auth='public', methods=['POST'], csrf=False) 
    # def get_debts_avg2(self, client_id, **args):
    #     return http.request.env['odata.1c.route'].get_by_route('1c_ut/debts_avg', client_id)

    