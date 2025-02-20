from odoo import models, fields, api
import openai

class ChatbotConversation(models.Model):
    _name = 'chatbot.conversation'  # Nombre del modelo
    _description = 'Conversación Chatbot'  # Descripción del modelo

    message = fields.Text(string='Mensaje')  # Campo para el mensaje del usuario
    response = fields.Text(string='Respuesta')  # Campo para la respuesta del chatbot

    # Función para enviar el mensaje a OpenAI y obtener la respuesta
    def send_message(self):
        # Obtener la clave API de los parámetros del sistema
        api_key = self.env['ir.config_parameter'].sudo().get_param('openai.api_key')
        if not api_key:
            raise ValueError("La clave API de OpenAI no está configurada en los parámetros del sistema.")
        
        openai.api_key = api_key
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.message,
            max_tokens=150
        )
        self.response = response.choices[0].text.strip()