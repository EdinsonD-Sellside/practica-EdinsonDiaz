{
    'name': 'Chatbot OpenAI',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Chatbot AI integrado con OpenAI',
    'description': 'Un chatbot basado en OpenAI para Odoo.',
    'author': 'Sellside',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/chatbot_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
