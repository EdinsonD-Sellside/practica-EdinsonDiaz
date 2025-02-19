{
    'name': 'OpenAI Chatbot',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Integración del chatbot de OpenAI en Odoo',
    'description': """Este módulo integra un chatbot de OpenAI en Odoo.""",
    'author': 'Tu Nombre',
    'website': 'https://tuweb.com',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/chatbot_views.xml',
        'data/chatbot_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'openai_chatbot/static/src/js/chatbot.js',
            'openai_chatbot/static/src/css/chatbot.css',
        ],
    },
    'installable': True,
    'application': True,
}
