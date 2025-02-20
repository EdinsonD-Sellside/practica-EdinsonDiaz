odoo.define('openai_chatbot.chat', function (require) {
    'use strict';
    const core = require('web.core');
    const _t = core._t;
    const rpc = require('web.rpc');

    $(document).ready(function() {
        $('#send_button').click(function() {
            const message = $('#chat_input').val();
            const conversation_id = $('.o_thread_viewport').data('res_id');

            rpc.query({
                model: 'openai_chatbot',
                method: 'send_message',
                args: [message, conversation_id],
            }).then(function(data) {
                if (data.error) {
                    console.error(data.error);
                    alert(_t("Error: ") + data.error);
                } else {
                    $('#chat_input').val(''); // Limpiar el input
                    // Recargar el widget mail_thread para mostrar el nuevo mensaje (usando un truco)
                    $('.o_thread_viewport').load(odoo.<ctrl61>odoo.info.r_prefix + '?debug=1 #', function() {
                        console.log('Chat actualizado.');
                    });
                }
            });
        });
    });
});