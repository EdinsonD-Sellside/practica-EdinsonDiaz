odoo.define('openai_custom_chatbot.chat', function (require) {
    "use strict";

    var core = require('web.core');
    var _t = core._t;
    var ajax = require('web.ajax');

    $('.o_chat_window').on('click', '.o_send_message', function () {
        var message = $('.o_chat_message').val();
        ajax.jsonRpc('/send_message', 'call', {
            'message': message
        }).then(function (data) {
            $('.o_chat_messages').append('<div class="o_chat_message o_chat_message_sent">' + message + '</div>');
            $('.o_chat_messages').append('<div class="o_chat_message o_chat_message_received">' + data.response + '</div>');
            $('.o_chat_message').val('');
        });
    });
});