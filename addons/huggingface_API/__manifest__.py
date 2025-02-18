{
    'name': 'Hugging Face Chatbot',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Chatbot basado en Hugging Face integrado en Odoo',
    'description': """Este módulo integra un chatbot de Hugging Face en Odoo.""",
    'author': 'Tu Nombre',
    'website': 'https://tuweb.com',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/chatbot_views.xml',
        'data/chatbot_data.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'huggingface_chatbot/static/src/js/chatbot.js',
            'huggingface_chatbot/static/src/css/chatbot.css'
        ],
    },
    'installable': True,
    'application': True,
}
