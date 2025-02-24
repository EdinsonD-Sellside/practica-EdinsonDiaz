from odoo import models
from openai import OpenAI
import logging

_logger = logging.getLogger(__name__)

class DiscussChannel(models.Model):
    _inherit = 'discuss.channel'

    def _message_post_after_hook(self, message, msg_vals):
        """Override to add AI response when needed"""
        result = super()._message_post_after_hook(message, msg_vals)
        
        # Only respond to human messages, not to AI ones
        if message.author_id != self.env.ref('chatgpt_openai.ai_assistant_partner'):
            self._handle_ai_response(message)
            
        return result

    def _handle_ai_response(self, message):
        """Handle AI response generation and posting"""
        try:
            # Get API key from system parameters
            api_key = self.env['ir.config_parameter'].sudo().get_param('openai.api_key')
            if not api_key:
                return

            # Initialize OpenAI client
            client = OpenAI(api_key=api_key)

            # Build message history for context
            messages = [{"role": "system", "content": "You are a helpful assistant."}]
            
            # Get recent message history for context
            domain = [
                ('model', '=', 'discuss.channel'),
                ('res_id', '=', self.id),
                ('message_type', '=', 'comment')
            ]
            history = self.env['mail.message'].search(domain, limit=10, order='id desc')
            
            # Add message history as context
            for msg in reversed(history):
                role = "assistant" if msg.author_id == self.env.ref('chatgpt_openai.ai_assistant_partner') else "user"
                messages.append({
                    "role": role,
                    "content": msg.body.strip()
                })

            # Get AI response
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Post AI response
            ai_message = completion.choices[0].message.content.strip()
            self.with_user(self.env.ref('chatgpt_openai.ai_assistant_user')).message_post(
                body=ai_message,
                message_type='comment',
                subtype_xmlid='mail.mt_comment'
            )

        except Exception as e:
            _logger.error("Error in AI response: %s", str(e))