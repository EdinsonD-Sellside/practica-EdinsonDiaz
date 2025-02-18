from odoo import http
from odoo.http import request
import json

class ChatbotController(http.Controller):

    @http.route('/huggingface/chatbot', type='json', auth='public', methods=['POST'], csrf=False)
    def chatbot_response(self, **kwargs):
        message = kwargs.get('message', '')
        chatbot_model = request.env['huggingface.chatbot'].sudo()
        response = chatbot_model.get_response(message)
        return json.dumps({"response": response})
