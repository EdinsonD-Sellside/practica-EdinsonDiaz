from odoo import models, fields, api
import openai

class ChatbotMessage(models.Model):
    _name = 'chatbot.message'
    _description = 'Chatbot Message'

    name = fields.Char(string='Message', required=True)
    response = fields.Text(string='Response')
    state = fields.Selection([
        ('new', 'New'),
        ('sent', 'Sent'),
        ('received', 'Received'),
    ], string='State', default='new')

    @api.model
    def create(self, values):
        record = super(ChatbotMessage, self).create(values)
        if record.state == 'new':
            record.send_message_to_openai()
        return record

    def send_message_to_openai(self):
        for record in self:
            openai.api_key = 'YOUR_OPENAI_API_KEY'
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=record.name,
                max_tokens=150
            )
            record.response = response.choices[0].text.strip()
            record.state = 'received'