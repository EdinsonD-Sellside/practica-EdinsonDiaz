{
    'name': 'OpenAI Chatbot',
    'version': '1.0',
    'category': 'Tools',
    'description': """
        Módulo para integrar un chatbot basado en OpenAI en Odoo.
    """,
    'author': 'EdinsonD',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/chatbot_views.xml',
    ],
    'installable': True,
    'application': True,
}
