# -*- coding: utf-8 -*-
{
    'name': "modulo_gemini",

    'summary': "Integración de la API de Gemini con Odoo",

    'description': """
Este módulo permite integrar la API de Gemini para generar contenido en base a texto y usarlo dentro de Odoo.
    """,

    'author': "Mi Empresa",
    'website': "https://www.miempresa.com",

    'category': 'Custom',  # Puedes cambiar la categoría a algo más específico si lo deseas
    'version': '1.0',  # Si ya estás listo para la versión 1.0

    'depends': ['base'],  # Dependencias mínimas necesarias para el módulo

    'data': [
        'views/views.xml',  # Asegúrate de que las vistas estén bien configuradas
        # Si no necesitas templates.xml, puedes comentarlo
        'views/templates.xml',  
    ],

    'demo': [
        'demo/demo.xml',  # Si tienes un archivo demo, inclúyelo aquí
    ],
}

