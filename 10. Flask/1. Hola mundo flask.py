# 1. Importar la clase Flask
from flask import Flask

# 2. Crear una instancia de la aplicación
app = Flask(__name__)

# 3. Definir una ruta y la función que se ejecutará
@app.route('/')
def hola_mundo():
    return '¡Hola desde Flask!'

if __name__ == '__main__':
    app.run(debug=True)