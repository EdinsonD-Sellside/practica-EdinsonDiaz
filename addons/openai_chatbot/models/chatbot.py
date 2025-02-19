from odoo import models, fields, api
import openai

class MiModuloChatbot(models.Model):
    _name = 'mi.modulo.chatbot'

    @api.model
    def obtener_api_key_openai(self):
        # Obtener la clave API de OpenAI desde los parámetros del sistema
        api_key = self.env['ir.config_parameter'].sudo().get_param('openai.api_key')
        
        # Configurar la API de OpenAI con la clave obtenida
        openai.api_key = api_key

        return api_key

    def generar_respuesta_chatbot(self, prompt):
        # Obtener la clave de la API
        self.obtener_api_key_openai()

        # Realizar una solicitud a la API de OpenAI
        response = openai.Completion.create(
            model="text-davinci-003",  # O cualquier modelo que estés usando
            prompt=prompt,
            max_tokens=150
        )

        return response.choices[0].text.strip()
