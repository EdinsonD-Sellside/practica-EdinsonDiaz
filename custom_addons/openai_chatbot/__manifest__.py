{
    'name': 'OpenAI Chatbot',
    'version': '1.0',
    'summary': 'Chatbot integrado con OpenAI',
    'description': 'Módulo para interactuar con la API de OpenAI',
    'author': 'Tu nombre',
    'depends': ['base', 'web'],  # Dependencias del módulo
    'data': [
        'security/ir.model.access.csv',
        'views/chatbot_views.xml',
        'data/chatbot_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}