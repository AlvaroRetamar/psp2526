import requests

url = "https://httpbin.org/post"

# Datos que queremos enviar al servidor
nuevo_post = {
    "titulo": "Mi primer post con Python",
    "contenido": "Requests hace que las APIs sean fáciles.",
    "id_usuario": 42
}

headers = {
    "User-Agent": "PSP retamar",
    "Content-Type": "application/json" # esto no es necesario, requests lo añade automáticamente
}

# Enviando la información mediante POST
response = requests.post(url, json=nuevo_post, headers=headers)

if response.status_code == 201 or response.status_code == 200:
    print("¡Recurso creado con éxito!")
    print("Respuesta del servidor:", response.json()['json'])