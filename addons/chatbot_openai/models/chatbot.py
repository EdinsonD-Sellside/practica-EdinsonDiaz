from odoo import models, fields, api
import openai

class ChatbotOpenAI(models.Model):
    _name = 'chatbot.openai'
    _description = 'Chatbot OpenAI'

    user_message = fields.Text(string="User Message")
    bot_response = fields.Text(string="Bot Response")

    @api.model
    def get_openai_response(self, user_message):
        """Obtiene una respuesta del asistente de OpenAI basado en el mensaje del usuario"""

        # Obtener la clave API de OpenAI desde los parámetros del sistema
        api_key = self.env['ir.config_parameter'].sudo().get_param('openai.api_key')

        if not api_key:
            return "Error: No se ha encontrado la clave API de OpenAI en los parámetros del sistema."

        try:
            # Configurar OpenAI con la API Key
            openai.api_key = api_key

            # Llamar a la API de OpenAI usando el asistente creado
            response = openai.beta.threads.create_and_run(
                assistant_id="asst_hPZ8aamUiwbNVRglCGOnJmQX",  # ID de tu asistente
                messages=[{"role": "user", "content": user_message}]
            )

            # Retornar la respuesta del asistente
            return response['output']['choices'][0]['message']['content']

        except openai.OpenAIError as e:
            return f"Error de OpenAI: {str(e)}"
        except Exception as e:
            return f"Error inesperado: {str(e)}"
