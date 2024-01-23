from odoo import models, fields, api

class ApiDocumentation(models.Model):
    _name = 'api.documentation'
    _description = 'API Documentation'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    endpoint_ids = fields.One2many(
        comodel_name='api.endpoint',
        inverse_name='documentation_id',
        string='API Endpoints'
    )

    @api.model
    def create_documentation(self, values):
        return self.create(values)

    def write_documentation(self, values):
        return self.write(values)

    def unlink_documentation(self):
        return self.unlink()

    def toggle_active(self):
        self.active = not self.active

class ApiEndpoint(models.Model):
    _name = 'api.endpoint'
    _description = 'API Endpoint'

    name = fields.Char(string='Endpoint Name', required=True)
    route = fields.Char(string='Route', required=True)
    method = fields.Selection(
        selection=[('get', 'GET'), ('post', 'POST'), ('put', 'PUT'), ('delete', 'DELETE')],
        string='Method',
        required=True
    )
    documentation_id = fields.Many2one(
        comodel_name='api.documentation',
        string='API Documentation',
        ondelete='cascade'
    )
    parameter_ids = fields.One2many(
        comodel_name='api.parameter',
        inverse_name='endpoint_id',
        string='Parameters'
    )
    response_ids = fields.One2many(
        comodel_name='api.response',
        inverse_name='endpoint_id',
        string='Responses'
    )

    def execute_endpoint(self, params):
        # Placeholder for endpoint execution logic
        pass

class ApiParameter(models.Model):
    _name = 'api.parameter'
    _description = 'API Parameter'

    name = fields.Char(string='Parameter Name', required=True)
    data_type = fields.Selection(
        selection=[('string', 'String'), ('integer', 'Integer'), ('boolean', 'Boolean'), ('object', 'Object')],
        string='Data Type',
        required=True
    )
    required = fields.Boolean(string='Required')
    default_value = fields.Char(string='Default Value')
    description = fields.Text(string='Description')
    endpoint_id = fields.Many2one(
        comodel_name='api.endpoint',
        string='API Endpoint',
        ondelete='cascade'
    )

class ApiResponse(models.Model):
    _name = 'api.response'
    _description = 'API Response'

    name = fields.Char(string='Response Name', required=True)
    response_code = fields.Integer(string='Response Code', required=True)
    description = fields.Text(string='Description')
    endpoint_id = fields.Many2one(
        comodel_name='api.endpoint',
        string='API Endpoint',
        ondelete='cascade'
    )
    body = fields.Text(string='Response Body')