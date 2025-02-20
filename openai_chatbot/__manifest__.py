{
    'name': 'OpenAI Chatbot',
    'version': '1.0',
    'summary': 'Integración con OpenAI GPT-4 para chatbot',
    'description': 'Este módulo integra OpenAI GPT-4 en Odoo para proporcionar funcionalidad de chatbot.',
    'author': 'Tu Nombre',
    'depends': ['base'],
    'data': [
        'views/chatbot_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}