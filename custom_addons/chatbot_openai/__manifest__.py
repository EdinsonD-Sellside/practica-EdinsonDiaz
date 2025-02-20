{
    'name': 'Chatbot OpenAI',  # Nombre de tu módulo
    'version': '1.0',  # Versión del módulo
    'summary': 'Integración de OpenAI para chatbot',  # Descripción breve
    'description': """
        Módulo para integrar la API de OpenAI y crear un chatbot en Odoo.
    """,  # Descripción detallada
    'author': 'Edinson D-Sellside',  # Tu nombre
    'depends': ['base'],  # Módulos de los que depende (si hay)
    'data': [
        'security/ir.model.access.csv',  # Archivos de seguridad
        'views/views.xml',  # Archivos de vistas
    ],
    'application': True,  # Indica que es una aplicación
    'installable': True,  # Permite la instalación
    'license': 'LGPL-3',  # Licencia del módulo
}