from odoo import models, fields, api

class ChatbotConversation(models.Model):
    _name = 'chatbot.conversation'
    _description = 'Chatbot Conversation'

    user_id = fields.Many2one('res.users', string='User', required=True)
    messages = fields.One2many('chatbot.message', 'conversation_id', string='Messages')
    create_date = fields.Datetime(string='Created on', default=fields.Datetime.now)

class ChatbotMessage(models.Model):
    _name = 'chatbot.message'
    _description = 'Chatbot Message'

    conversation_id = fields.Many2one('chatbot.conversation', string='Conversation', required=True, ondelete='cascade')
    sender = fields.Selection([('user', 'User'), ('bot', 'Bot')], string='Sender', required=True)
    message = fields.Text(string='Message', required=True)
    timestamp = fields.Datetime(string='Timestamp', default=fields.Datetime.now)