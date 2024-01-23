odoo.define('odoo_external_api_access.api_interactive_explorer', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
    var ajax = require('web.ajax');
    var Dialog = require('web.Dialog');

    var QWeb = core.qweb;
    var _t = core._t;

    var ApiInteractiveExplorer = Widget.extend({
        template: 'ApiInteractiveExplorerTemplate',
        events: {
            'click .o_api_explore_endpoint': '_onExploreEndpoint',
            'click .o_api_execute_endpoint': '_onExecuteEndpoint',
            'click .o_api_export_documentation': '_onExportDocumentation',
        },

        init: function (parent, options) {
            this._super(parent);
            this.options = options || {};
        },

        start: function () {
            var self = this;
            this._super.apply(this, arguments);
            this._loadEndpoints();
        },

        _loadEndpoints: function () {
            var self = this;
            ajax.jsonRpc("/api/documentation", 'call', {}).then(function (data) {
                self.$el.find('#' + apiEndpointList).html(QWeb.render('ApiEndpointsList', {endpoints: data}));
            });
        },

        _onExploreEndpoint: function (event) {
            var endpointId = $(event.currentTarget).data('endpoint-id');
            this._exploreApiEndpoint(endpointId);
        },

        _exploreApiEndpoint: function (endpointId) {
            var self = this;
            ajax.jsonRpc("/api/explore", 'call', {endpoint_id: endpointId}).then(function (data) {
                self.$el.find('#' + apiExplorerContainer).html(QWeb.render('ApiExplorer', {endpoint: data}));
            });
        },

        _onExecuteEndpoint: function (event) {
            var endpointId = $(event.currentTarget).data('endpoint-id');
            var params = this.$el.find('#' + apiRequestForm).serializeArray();
            this._executeApiEndpoint(endpointId, params);
        },

        _executeApiEndpoint: function (endpointId, params) {
            var self = this;
            ajax.jsonRpc("/api/execute", 'call', {endpoint_id: endpointId, params: params}).then(function (response) {
                self.$el.find('#' + apiResponseDisplay).text(JSON.stringify(response, null, 2));
                if (response.error) {
                    self.do_notify(_t('API Execution Failed'), response.error, true);
                } else {
                    self.do_notify(_t('API Execution Succeeded'), _t('The API call was successful.'), false);
                }
            }).guardedCatch(function (error) {
                self.do_notify(_t('API Execution Failed'), _t('An error occurred during the API call.'), true);
            });
        },

        _onExportDocumentation: function () {
            window.location = '/api/documentation/export';
        },
    });

    core.action_registry.add('api_interactive_explorer', ApiInteractiveExplorer);

    return ApiInteractiveExplorer;
});