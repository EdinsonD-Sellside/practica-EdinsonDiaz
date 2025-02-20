from odoo import models, fields, api
import openai

class ChatbotConversation(models.Model):
    _name = 'chatbot.conversation'
    _description = 'Conversación Chatbot'

    message = fields.Text(string='Mensaje')
    response = fields.Text(string='Respuesta')

    @api.model
    def _get_openai_api_key(self):
        # Obtiene la API key de OpenAI de los parámetros del sistema
        return self.env['ir.config_parameter'].sudo().get_param('openai.api_key')

    def send_message(self):
        openai.api_key = self._get_openai_api_key()  # Configura la API key de OpenAI
        
        # Envía el mensaje a OpenAI y recibe la respuesta
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Puedes ajustar el modelo aquí
                prompt=self.message,
                max_tokens=150  # Puedes ajustar la longitud de la respuesta
            )
            self.response = response.choices[0].text.strip()  # Guarda la respuesta en el campo 'response'
        except Exception as e:
            self.response = f"Error al contactar a OpenAI: {e}"  # Maneja los errores de la API

    # Botón para enviar el mensaje
    def _send_message_button(self):
        self.send_message()
