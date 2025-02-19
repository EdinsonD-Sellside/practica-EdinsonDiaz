from odoo import http
from odoo.http import request
import openai

class ChatbotController(http.Controller):
    @http.route('/chatbot_openai/ask', type='http', auth='public', methods=['POST'], csrf=False)
    def ask_chatbot(self, message, **kw):
        openai_api_key = request.env['ir.config_parameter'].sudo().get_param('openai.api_key')

        if not openai_api_key:
            return "Error: Clave de API de OpenAI no configurada."

        openai.api_key = openai_api_key

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=150,
        )

        answer = response.choices[0].text.strip()

        request.env['chatbot.conversation'].sudo().create({
            'message': message,
            'response': answer,
        })

        return answer