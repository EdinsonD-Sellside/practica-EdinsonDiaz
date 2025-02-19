{
    'name': 'Chatbot OpenAI',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Un chatbot basado en OpenAI',
    'description': 'Este módulo integra OpenAI para crear un chatbot dentro de Odoo.',
    'author': 'EdinsonD',
    'depends': ['base'],
    'data': [
        'views/chatbot_openai_view.xml',
    ],
    'installable': True,
    'application': True,
}
