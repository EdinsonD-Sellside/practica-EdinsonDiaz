from odoo import models, fields, api
import requests

class Chatbot(models.Model):
    _name = 'huggingface.chatbot'
    _description = 'Chatbot basado en Hugging Face'

    name = fields.Char(string="Nombre", required=True)
    message = fields.Text(string="Mensaje")
    response = fields.Text(string="Respuesta del Chatbot", readonly=True)

    @api.model
    def get_response(self, message):
        """Llamada a Hugging Face API para obtener respuesta"""
        api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        headers = {"Authorization": "Bearer TU_TOKEN_HUGGINGFACE"}
        payload = {"inputs": message}

        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json().get('generated_text', 'No se obtuvo respuesta')
        return "Error en la respuesta del chatbot"
