import requests

# Enviar parámetros en una solicitud GET
diccionario_de_parametros = {'usuario': 'este "value+" 1', 'opcion': 'value 2'}
cabeceras_personalizadas = {'User-Agent': 'Valor de mi cabecera'}
respuesta = requests.get('https://httpbin.org/get', params=diccionario_de_parametros, headers=cabeceras_personalizadas)
print(respuesta.url)
print(respuesta.request.headers)