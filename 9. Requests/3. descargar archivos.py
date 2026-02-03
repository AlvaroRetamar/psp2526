import requests

# URL de una imagen aleatoria (un perrito, por ejemplo)
image_url = "https://placedog.net/500"

print("Descargando imagen...")
response = requests.get(image_url)

if response.status_code == 200:
    # Abrimos un archivo local en modo 'wb' (write binary)
    with open("perrito_descargado.jpg", "wb") as f:
        # Escribimos el contenido de la respuesta en el archivo
        f.write(response.content)
    print("Imagen guardada como 'perrito_descargado.jpg'")
else:
    print(f"No se pudo descargar la imagen. Código de error: {response.status_code}")


# Ahora lo mismo pero con un archivo muy grande --> usando streaming
large_file_url = "https://nbg1-speed.hetzner.com/100MB.bin"
print("Descargando archivo grande con streaming...")
with requests.get(large_file_url, stream=True) as response:
    if response.status_code == 200:
        with open("archivo_grande_descargado.bin", "wb") as f:
            # Iteramos sobre el contenido en bloques de 1MB
            for chunk in response.iter_content(chunk_size=1024*1024):
                if chunk:  # Filtramos los bloques vacíos
                    f.write(chunk)
        print("Archivo grande guardado como 'archivo_grande_descargado.bin'")