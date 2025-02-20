{
    'name': 'OpenAI Chatbot',
    'version': '1.0',
    'summary': 'Integración con OpenAI GPT-4 para chatbot',
    'description': 'Este módulo integra OpenAI GPT-4 en Odoo para proporcionar funcionalidad de chatbot.',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/chatbot_view.xml',
        'views/chatbot_config_view.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'openai_chatbot/static/src/js/chat.js',
        ],
    },
}