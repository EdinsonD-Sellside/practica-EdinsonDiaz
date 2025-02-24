from odoo import models, fields, api
import openai

class CustomChatbot(models.Model):
    _name = 'openai_custom_chatbot.chatbot'  # Nombre del modelo
    _description = 'Custom Chatbot OpenAI'  # Descripción del modelo

    message = fields.Text(string='Mensaje')  # Campo para el mensaje
    response = fields.Text(string='Respuesta')  # Campo para la respuesta

    def send_message(self):
        # Obtiene la API Key de OpenAI desde los parámetros del sistema
        openai.api_key = self.env['ir.config_parameter'].get_param('openai.api_key')
        # Llama a la API de OpenAI para obtener una respuesta
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Modelo de OpenAI a utilizar
            prompt=self.message,  # Mensaje a enviar a OpenAI
            max_tokens=150  # Cantidad máxima de tokens en la respuesta
        )
        # Guarda la respuesta de OpenAI en el campo response
        self.response = response.choices[0].text.strip()