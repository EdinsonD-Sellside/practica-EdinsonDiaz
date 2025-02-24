{
    'name': 'Custom Chatbot OpenAI',
    'version': '1.0',
    'depends': ['base', 'mail', 'im_livechat', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'openai_custom_chatbot/static/src/js/chat.js'
        ],
        'web.assets_qweb': [
            'openai_custom_chatbot/static/src/xml/chat.xml'
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'external_dependencies': {
        'python': ['openai'],
    },
}