{
    'name': 'OpenAI Chatbot',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Integration with OpenAI Chatbot',
    'description': """Integration with OpenAI Chatbot to send and receive messages.""",
    'author': 'Your Name',
    'website': 'http://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/chatbot_views.xml',
    ],
    'installable': True,
    'application': True,
}