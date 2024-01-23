from odoo import api, fields, models
from odoo.exceptions import AccessError, UserError

class ApiExecutionWizard(models.TransientModel):
    _name = 'api.execution.wizard'
    _description = 'API Execution Wizard'

    api_endpoint_id = fields.Many2one('api.endpoint', string='API Endpoint', required=True)
    request_data = fields.Text(string='Request Data')
    response_data = fields.Text(string='Response Data', readonly=True)

    @api.model
    def default_get(self, fields):
        res = super(ApiExecutionWizard, self).default_get(fields)
        context = self.env.context
        if 'default_api_endpoint_id' in context:
            res['api_endpoint_id'] = context['default_api_endpoint_id']
        return res

    def execute_api_endpoint(self):
        self.ensure_one()
        if not self.api_endpoint_id:
            raise UserError('No API Endpoint selected for execution.')

        # Simulate API request based on the selected endpoint and provided request data
        try:
            # Here you would integrate with the actual API execution logic
            # For demonstration purposes, we'll just simulate a response
            simulated_response = '{"success": true, "data": "Simulated response data"}'
            self.response_data = simulated_response
            self.env['api.history'].create({
                'api_endpoint_id': self.api_endpoint_id.id,
                'request_data': self.request_data,
                'response_data': self.response_data,
            })
        except Exception as e:
            raise UserError('API Execution Failed: %s' % str(e))

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'api.execution.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }