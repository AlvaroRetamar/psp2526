import requests

# 1. El método GET: Consultar información
url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url)
    
    # Verificar si la petición fue exitosa (Status Code 200)
    # Si no lo fue, este método lanzará una excepción HTTPError
    response.raise_for_status() 
    
    # Convertir la respuesta JSON en un diccionario de Python
    print('--- Tipo de Datos ---')
    print(type(response))  # <class 'requests.models.Response'>
    user_data = response.json()
    print(type(user_data))  # <class 'dict'>
    print(user_data.keys())
    
    print("--- Usuario Encontrado ---")
    print(f"Nombre: {user_data['name']}")
    print(f"Email:  {user_data['email']}")
    print(f"Ciudad: {user_data['address']['city']}")

except requests.exceptions.HTTPError as err:
    print(f"Error HTTP: {err}")