import requests
from odoo import models, fields, api

class HuggingFaceModel(models.Model):
    _name = 'huggingface.model'
    _description = 'Modelo de integración con Hugging Face'

    name = fields.Char(string="Nombre", required=True)

    def call_huggingface_api(self):
        # Llama a la API de Hugging Face
        url = "https://api-inference.huggingface.co/models/gpt2"  # Modelo GPT-2 como ejemplo
        headers = {
            "Authorization": f"Bearer {self.env['ir.config_parameter'].get_param('huggingface_api_key')}"
        }

        # La entrada para el modelo puede variar, aquí ejemplo con un mensaje simple
        data = {"inputs": "Hola, ¿cómo estás?"}

        try:
            response = requests.post(url, headers=headers, json=data)

            # Si la respuesta es correcta, extraemos el resultado
            if response.status_code == 200:
                result = response.json()
                return result  # Puedes ajustar esto dependiendo del formato de la respuesta
            else:
                # Si no es 200, lanzamos un error con el mensaje de la API
                error_message = response.json().get('error', 'Error desconocido')
                raise ValueError(f"Error al llamar a la API de Hugging Face: {error_message}")

        except requests.exceptions.RequestException as e:
            # Captura cualquier excepción relacionada con la conexión o HTTP
            raise ValueError(f"Excepción al conectar con la API: {e}")

