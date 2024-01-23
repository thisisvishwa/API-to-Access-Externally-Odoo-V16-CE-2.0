from odoo import http
from odoo.http import request

class ExternalAPIController(http.Controller):

    @http.route('/api/documentation', auth='user', type='http', website=True)
    def api_documentation(self, **kwargs):
        api_documentation = request.env['api.documentation'].search([])
        return request.render('odoo_external_api_access.api_documentation_template', {
            'api_documentation': api_documentation,
        })

    @http.route('/api/execute', auth='user', type='json', methods=['POST'], csrf=False)
    def execute_api(self, model, method, args, kwargs):
        Model = request.env[model]
        if hasattr(Model, method):
            try:
                result = getattr(Model, method)(*args, **kwargs)
                return {'success': True, 'result': result}
            except Exception as e:
                return {'success': False, 'error': str(e)}
        else:
            return {'success': False, 'error': 'Method not found'}

    @http.route('/api/explore', auth='user', type='http', website=True)
    def explore_api(self, endpoint_id):
        endpoint = request.env['api.endpoint'].browse(int(endpoint_id))
        if not endpoint.exists():
            return request.not_found()
        return request.render('odoo_external_api_access.api_explorer_template', {
            'endpoint': endpoint,
        })

    @http.route('/api/history', auth='user', type='http', website=True)
    def api_history(self, **kwargs):
        history = request.env['api.history'].search([])
        return request.render('odoo_external_api_access.api_history_template', {
            'history': history,
        })

    @http.route('/api/favorites', auth='user', type='http', website=True)
    def api_favorites(self, **kwargs):
        favorites = request.env['api.favorites'].search([])
        return request.render('odoo_external_api_access.api_favorites_template', {
            'favorites': favorites,
        })