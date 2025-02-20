{
    'name': 'OpenAI Chatbot',
    'version': '1.0',
    'summary': 'Chatbot integrado con OpenAI',
    'description': 'Módulo para interactuar con la API de OpenAI',
    'author': 'Tu nombre',
    'depends': ['base'],  # Dependencia del módulo base de Odoo
    'data': [
        'views/openai_chatbot_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}