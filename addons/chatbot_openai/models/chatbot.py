from odoo import models, fields, api
import openai

class ChatbotOpenAI(models.Model):
    _name = 'chatbot.openai'
    _description = 'Chatbot OpenAI'

    user_message = fields.Text(string="User Message")
    bot_response = fields.Text(string="Bot Response")
    
    @api.model
    def get_openai_response(self, user_message):
        # Obtener la clave API de OpenAI desde los parámetros del sistema
        api_key = self.env['ir.config_parameter'].sudo().get_param('openai.api_key')
        
        if not api_key:
            return "Error: No se ha encontrado la clave API de OpenAI en los parámetros del sistema."
        
        # Configura tu clave API de OpenAI
        openai.api_key = api_key

        try:
            # Realiza la llamada a la API de OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # O el modelo que estés utilizando
                messages=[
                    {"role": "system", "content": "Eres un asistente útil."},
                    {"role": "user", "content": user_message}
                ]
            )
            # Retorna la respuesta generada por el modelo
            return response['choices'][0]['message']['content']
        except Exception as e:
            # Manejo de errores
            return f"Error al obtener respuesta de OpenAI: {str(e)}"
