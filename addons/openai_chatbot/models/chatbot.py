import requests
from odoo import models, fields, api

class Chatbot(models.Model):
    _name = 'openai.chatbot'
    _description = 'Chatbot basado en OpenAI'

    name = fields.Char(string="Nombre", required=True)
    message = fields.Text(string="Mensaje")
    response = fields.Text(string="Respuesta del Chatbot", readonly=True)

    @api.model
    def get_response(self, message):
        """Llama a OpenAI para obtener la respuesta del chatbot"""
        api_key = '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'  # Asegúrate de poner tu API Key aquí
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": message}]
        }

        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error en respuesta")
        else:
            return f"Error: {response.status_code} - {response.text}"
