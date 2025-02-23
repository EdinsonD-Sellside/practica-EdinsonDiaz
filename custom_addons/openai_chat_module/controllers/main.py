from odoo import http, exceptions
from odoo.http import request
import openai

class ChatbotController(http.Controller):

    @http.route('/openai_chat_module/send_message', type='json', auth='user')
    def send_message(self, message):
        try:
            # Obtener la API key desde los parámetros del sistema
            api_key = request.env['ir.config_parameter'].sudo().get_param('openai.api_key')
            if not api_key:
                raise exceptions.UserError("API key de OpenAI no configurada.")

            openai.api_key = api_key

            # Interactuar con la API de OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Puedes ajustar el modelo aquí
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": message},
                ]
            )
            answer = response.choices[0].message['content']
            return {'answer': answer}

        except Exception as e:
            return {'error': str(e)}