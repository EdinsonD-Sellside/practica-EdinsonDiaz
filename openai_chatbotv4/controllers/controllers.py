from odoo import http
from odoo.http import request
import openai

class OpenAIChatbot(http.Controller):

    @http.route('/chatbot', type='json', auth='public')
    def chatbot(self, message):
        api_key = request.env['ir.config_parameter'].sudo().get_param('openai.api_key')
        openai.api_key = api_key

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message['content']