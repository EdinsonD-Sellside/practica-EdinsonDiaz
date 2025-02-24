{
    'name': 'IA_openai_chatbot_2025_1-link',
    'version': '1.0',
    'author': 'Edinson',
    'depends': ['base', 'mail'],
    'data': [
        'data/ai_bot_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,  # No se instala automáticamente
    'external_dependencies': {
        'python': ['openai'],
    },
}
