from odoo import models, fields

class ChatbotConfig(models.Model):
    _name = 'chatbot.config'
    _description = 'Configuración del Chatbot'

    api_key = fields.Char(string='Clave API de OpenAI', required=True)