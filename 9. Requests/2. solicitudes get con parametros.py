import requests

# Enviar parámetros en una solicitud GET
payload = {'key1': 'value1', 'key2': 'value2'}
respuesta = requests.get('https://httpbin.org/get', params=payload)
print(respuesta.url)
print(respuesta.request.headers)