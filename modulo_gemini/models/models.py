# -*- coding: utf-8 -*-

from odoo import models, fields, api
from google import genai

class modulo_gemini(models.Model):
    _name = 'modulo_gemini.modulo_gemini'
    _description = 'Módulo que integra la API de Gemini'

    name = fields.Char(string="Name")
    value = fields.Integer(string="Value")
    value2 = fields.Float(string="Computed Value", compute="_value_pc", store=True)
    description = fields.Text(string="Description")
    
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def call_gemini_api(self):
        """Método para interactuar con la API de Gemini y obtener un contenido generado."""
        # Asegúrate de sustituir "YOUR_API_KEY" por tu clave de API real
        client = genai.Client(api_key="YOUR_API_KEY")
        
        # Realiza la solicitud a la API de Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents="Explain how AI works"
        )
        
        # Imprimir la respuesta de la API en la consola (o procesarla como desees)
        print(response.text)
        
        # Aquí podrías guardar la respuesta en algún campo del modelo si deseas
        # Por ejemplo, puedes almacenar el contenido generado en el campo description
        self.description = response.text
        
        return response.text

