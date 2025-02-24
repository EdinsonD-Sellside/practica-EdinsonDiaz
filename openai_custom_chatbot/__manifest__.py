{
    'name': 'Custom Chatbot OpenAI',  # Nombre del módulo
    'version': '1.0',  # Versión del módulo
    'depends': ['base', 'mail', 'im_livechat'],  # Dependencias necesarias, incluyendo el chat en vivo
    'data': [
        'security/ir.model.access.csv',  # Reglas de acceso
        'views/views.xml',  # Vistas del módulo
        'views/templates.xml',  # Plantillas web
    ],
    'assets': {
        'web.assets_backend': [
            'openai_custom_chatbot/static/src/js/chat.js'  # Archivo JS para el chat
        ],
        'web.assets_qweb': [
            'openai_custom_chatbot/static/src/xml/chat.xml',  # Archivo XML para el chat
        ],
    },
    'installable': True,  # Permite la instalación
    'application': True,  # Se muestra como aplicación
    'auto_install': False,  # No se instala automáticamente
    'license': 'LGPL-3',  # Licencia del módulo
    'external_dependencies': {
        'python': ['openai'],
    },
}