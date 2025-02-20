from odoo import http
from odoo.http import request

class ChatbotController(http.Controller):
    @http.route('/chatbot', type='http', auth='public', website=True)
    def chatbot(self, **kw):
        return request.render("chatbot_openai.chatbot_template", {
            'response': kw.get('response')
        })