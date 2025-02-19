from odoo import http
from odoo.http import request
import os
import openai
import json

class ChatbotController(http.Controller):

    @http.route('/openai/chatbot', type='json', auth='public', methods=['POST'], csrf=False)
    def chatbot_response(self, **kwargs):
        message = kwargs.get('message', '')
        response = self.get_openai_response(message)
        return json.dumps({"response": response})

    def get_openai_response(self, message):
        """ Llamada a la API de OpenAI para obtener respuesta """
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            return "API Key de OpenAI no configurada."

        openai.api_key = api_key
        
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # O usa el modelo que prefieras
                prompt=message,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error al obtener respuesta de OpenAI: {str(e)}"
