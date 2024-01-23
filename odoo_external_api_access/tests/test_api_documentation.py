from odoo.tests.common import TransactionCase

class TestAPIDocumentation(TransactionCase):

    def setUp(self):
        super(TestAPIDocumentation, self).setUp()
        self.api_documentation_model = self.env['api.documentation']

    def test_create_api_documentation(self):
        # Test the creation of API documentation
        api_doc = self.api_documentation_model.create({
            'name': 'Test API Documentation',
            'description': 'This is a test API documentation'
        })
        self.assertTrue(api_doc, "API Documentation was not created")

    def test_generate_api_documentation(self):
        # Test the generation of API documentation
        api_doc = self.api_documentation_model.create({
            'name': 'Test API Documentation',
            'description': 'This is a test API documentation'
        })
        api_doc.generate_api_documentation()
        self.assertTrue(api_doc.documentation_generated, "API Documentation was not generated")

    def test_api_documentation_access_rights(self):
        # Test the access rights for API documentation
        api_doc = self.api_documentation_model.create({
            'name': 'Test API Documentation',
            'description': 'This is a test API documentation'
        })
        with self.assertRaises(AccessError):
            self.api_documentation_model.with_user(self.ref('base.user_demo')).generate_api_documentation()

    def test_api_endpoint_execution(self):
        # Test the execution of an API endpoint from the documentation interface
        api_doc = self.api_documentation_model.create({
            'name': 'Test API Documentation',
            'description': 'This is a test API documentation'
        })
        response = api_doc.execute_api_endpoint('test_endpoint')
        self.assertEqual(response.status_code, 200, "API Endpoint did not execute successfully")

    def test_api_documentation_export(self):
        # Test the export functionality of API documentation
        api_doc = self.api_documentation_model.create({
            'name': 'Test API Documentation',
            'description': 'This is a test API documentation'
        })
        export_file = api_doc.export_api_documentation()
        self.assertTrue(export_file, "API Documentation was not exported")

    def tearDown(self):
        # Clean up after tests
        docs = self.api_documentation_model.search([])
        docs.unlink()
        super(TestAPIDocumentation, self).tearDown()