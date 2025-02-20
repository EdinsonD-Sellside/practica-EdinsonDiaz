{
    'name': 'Chatbot OpenAI',
    'version': '1.0',
    'description': 'Módulo para integrar la API de OpenAI y crear un chatbot en Odoo.',
    'author': 'EdinsonD',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  # Archivos de seguridad
        'views/views.xml',  # Archivos de vistas
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
