from odoo import models, fields, api
import openai

class CustomChatbot(models.Model):
    _name = 'openai_custom_chatbot.chatbot'
    _description = 'Custom Chatbot OpenAI'

    message = fields.Text(string='Mensaje')
    response = fields.Text(string='Respuesta')

    def send_message(self):
        openai.api_key = self.env['ir.config_parameter'].get_param('openai.api_key')
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=self.message,
            max_tokens=150
        )
        self.response = response.choices[0].text.strip()