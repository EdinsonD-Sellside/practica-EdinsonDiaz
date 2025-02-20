from odoo import http, api, exceptions
from odoo.http import request
import openai

class OpenAIChatbot(http.Controller):
    @http.route('/openai_chatbot/send_message', type='json', auth='user')
    def send_message(self, message, conversation_id=None, **kw):
        try:
            config = request.env['chatbot.config'].sudo().search([], limit=1)
            if not config:
                raise exceptions.UserError("No se ha configurado la API de OpenAI.")
            openai.api_key = config.api_key

            if conversation_id:
                conversation = request.env['mail.channel'].sudo().browse(conversation_id)
            else:
                conversation = request.env['mail.channel'].sudo().create({
                    'name': 'Chat con OpenAI',
                    'channel_type': 'chat',
                    'public': 'private',
                    'user_ids': [(6, 0, [request.uid])],
                })
                conversation_id = conversation.id

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # o gpt-4 si está disponible
                messages=[
                    {"role": "system", "content": "Eres un asistente virtual."},
                    {"role": "user", "content": message},
                ]
            )
            bot_message = response.choices[0].message.content

            conversation.message_post(body=message, message_type='comment', subtype_id=False)
            conversation.message_post(body=bot_message, message_type='comment', subtype_id=False)

            return {'message': bot_message, 'conversation_id': conversation_id}

        except Exception as e:
            return {'error': str(e)}