import requests

BASE_URL = 'http://127.0.0.1:5000/'

# Los datos que queremos enviar. La clave 'usuario' debe coincidir
# con lo que el servidor espera en 'request.form'.
datos_formulario = {
    'usuario': 'Alvaro Retamar'
}

# Hacemos la petición POST
# Usamos el argumento 'data' para enviar datos como un formulario.
# requests se encargará de codificarlo correctamente.
print("Enviando petición POST a:", BASE_URL + 'login')
response = requests.post(BASE_URL + 'login', data=datos_formulario) # como se manda un formulario HTML, se usa 'data' y no 'json'

# Comprobamos la respuesta del servidor
print("-" * 20)
print(f"Código de estado HTTP: {response.status_code}")

# La respuesta del servidor es HTML, así que la imprimimos como texto plano.
print(f"Respuesta (texto): {response.text}")


# Qué pasa si mandamos los datos como JSON en vez de como formulario?
print("\nEnviando petición POST con JSON a:", BASE_URL + 'login')
response_json = requests.post(BASE_URL + 'login', json=datos_formulario) # aquí usamos 'json' en vez de 'data'
# Comprobamos la respuesta del servidor para el JSON
print("-" * 20)
print(f"Código de estado HTTP: {response_json.status_code}")
print(f"Respuesta (texto): {response_json.text}")