Installation
============

This document provides instructions on how to install the Odoo External API Access Module, version 1.0, for Odoo 16 Community Edition.

Prerequisites
-------------

Before installing the module, ensure that you have the following:

- Odoo 16 Community Edition installed and running.
- Administrative access to the Odoo instance.
- The module's source code, available at [https://thisis.com](https://thisis.com).

Installation Steps
------------------

1. Download the module from the provided website:

   .. code-block:: shell

       wget https://thisis.com/odoo_external_api_access.zip

2. Unzip the module into the Odoo addons directory:

   .. code-block:: shell

       unzip odoo_external_api_access.zip -d /path/to/odoo/addons/

3. Update the Odoo module list:

   .. code-block:: shell

       /path/to/odoo/odoo-bin -c /path/to/odoo.conf -u base --stop-after-init

4. Log in to your Odoo instance as an administrator.

5. Navigate to the Apps menu and remove the 'Apps' filter in the search bar.

6. Search for 'odoo_external_api_access' in the search bar.

7. Click on the 'Install' button next to the module to start the installation process.

Post-Installation
-----------------

After installing the module, you may need to configure it to suit your needs:

1. Go to the Odoo backend interface.

2. Navigate to the 'Odoo External API Access' configuration menu.

3. Adjust the settings according to your requirements, as described in the `configuration.rst` document.

4. Save the changes.

You can now start using the Odoo External API Access Module to generate API documentation, explore APIs interactively, and execute API operations directly from the Odoo backend interface.

For more detailed information on configuration and usage, refer to the `configuration.rst` and `usage.rst` documents respectively.