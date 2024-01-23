{
    'name': 'Odoo External API Access',
    'version': '1.0',
    'summary': 'API Documentation and Interactive Exploration Module',
    'sequence': 10,
    'author': 'Vishwa G',
    'website': 'https://thisis.com',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/api_documentation_views.xml',
        'views/api_documentation_templates.xml',
        'data/api_data.xml',
        'demo/api_demo.xml',
    ],
    'demo': [
        'demo/api_demo.xml',
    ],
    'qweb': [
        'static/src/xml/api_documentation_snippets.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'odoo_external_api_access/static/src/js/api_interactive_explorer.js',
            'odoo_external_api_access/static/src/css/api_styles.css',
        ],
    },
    'images': ['static/description/icon.png'],
    'description': """
Odoo External API Access Module
==============================
This module provides dynamic API documentation generation, interactive exploration, and direct API operation execution within the Odoo backend interface.
    """,
}