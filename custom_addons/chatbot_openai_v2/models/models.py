from odoo import models, fields

class ChatbotConversation(models.Model):
    _name = 'chatbot.conversation'
    _description = 'Conversación del Chatbot'

    message = fields.Text('Mensaje')
    response = fields.Text('Respuesta')