from odoo import http

class CustomChatbot(http.Controller):
    @http.route('/chat', auth='public', website=True)
    def chat(self, **kw):
        return http.request.render('openai_custom_chatbot.chat_template', {
            'response': kw.get('response')
        })

    @http.route('/send_message', auth='public', website=True, methods=['POST'])
    def send_message(self, **kw):
        message = kw.get('message')
        openai.api_key = http.request.env['ir.config_parameter'].get_param('openai.api_key')
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=message,
            max_tokens=150
        )
        response_text = response.choices[0].text.strip()
        return http.redirect('/chat?response=' + response_text)