from odoo import models, fields, api

class ChatbotConfig(models.Model):
    _name = 'chatbot.config'
    _description = 'Configuración del Chatbot'

    api_key = fields.Char(string='Clave API de OpenAI', required=True)

    @api.model
    def _install(self):
        super(ChatbotConfig, self)._install()
        # Crear los registros de acceso si no existen.  (Evita duplicados)
        access_model_chatbot_config = self.env.ref('openai_chatbot.access_chatbot_config') # Reemplaza 'tu_modulo' con el nombre de tu módulo
        if not access_model_chatbot_config: # Si no existe el registro
            self.env['ir.model.access'].create({
                'name': 'access_chatbot_config',
                'model_id': self.env.ref('openai_chatbot.model_chatbot_config').id,  # Reemplaza 'tu_modulo'
                'group_id': self.env.ref('base.group_user').id,
                'perm_read': 1,
                'perm_write': 1,
                'perm_create': 1,
                'perm_unlink': 1,
            })
        access_mail_channel = self.env.ref('openai_chatbot.access_mail_channel') # Reemplaza 'tu_modulo' con el nombre de tu módulo
        if not access_mail_channel: # Si no existe el registro
            self.env['ir.model.access'].create({
                'name': 'access_mail_channel',
                'model_id': self.env.ref('model_mail_channel').id,
                'group_id': self.env.ref('base.group_user').id,
                'perm_read': 1,
                'perm_write': 1,
                'perm_create': 1,
                'perm_unlink': 1,
            })