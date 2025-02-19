odoo.define('openai_chatbot.chatbot', function(require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.ChatbotWidget = publicWidget.Widget.extend({
        selector: '.chatbot-container',
        events: {
            'click .send-btn': '_onSendMessage',
        },

        _onSendMessage: function(ev) {
            var self = this;
            var message = this.$('.chat-input').val();
            if (!message) return;

            this._rpc({
                route: '/openai/chatbot',
                params: { message: message }
            }).then(function(result) {
                var response = JSON.parse(result).response;
                self.$('.chat-response').text(response);
            });
        }
    });

    return publicWidget.registry.ChatbotWidget;
});
