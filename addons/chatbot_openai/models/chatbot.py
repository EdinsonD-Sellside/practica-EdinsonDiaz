import openai
from odoo import models, fields, api

class ChatbotOpenAI(models.Model):
    _name = 'chatbot.openai'
    _description = 'Chatbot OpenAI'

    user_message = fields.Text(string="User Message")
    bot_response = fields.Text(string="Bot Response")
    
    @api.model
    def get_openai_response(self, user_message):
        # Obtener la API Key desde los parámetros del sistema
        api_key = self.env['ir.config_parameter'].sudo().get_param('openai.api_key')
        
        if not api_key:
            return "Error: No se encontró la clave API en Odoo."

        openai.api_key = api_key

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "Eres un asistente útil."},
                          {"role": "user", "content": user_message}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error al conectar con OpenAI: {str(e)}"
