from odoo import models, fields, api
import openai

class ChatbotOpenAI(models.Model):
    _name = 'chatbot.openai'
    _description = 'Chatbot OpenAI'

    user_message = fields.Text(string="Mensaje del Usuario")
    bot_response = fields.Text(string="Respuesta del Bot")

    @api.model
    def get_openai_response(self, user_message):
        """Obtiene una respuesta de OpenAI basada en el mensaje del usuario"""
        
        # Obtener la clave API de OpenAI desde los parámetros del sistema
        api_key = self.env['ir.config_parameter'].sudo().get_param('openai.api_key')

        if not api_key:
            return "Error: No se ha encontrado la clave API de OpenAI en los parámetros del sistema."

        try:
            # Configurar la clave API en OpenAI
            openai.api_key = api_key

            # Realizar la llamada a la API de OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un asistente útil."},
                    {"role": "user", "content": user_message}
                ]
            )

            # Retornar la respuesta generada por el modelo
            return response['choices'][0]['message']['content']

        except openai.OpenAIError as e:
            return f"Error de OpenAI: {str(e)}"
        except Exception as e:
            return f"Error inesperado: {str(e)}"

    def get_bot_response(self):
        """Llama a OpenAI y guarda la respuesta en el campo bot_response"""
        
        for record in self:
            if not record.user_message:
                return {'warning': {'title': "Error", 'message': "Debes ingresar un mensaje."}}

            response_text = record.get_openai_response(record.user_message)
            record.bot_response = response_text

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
