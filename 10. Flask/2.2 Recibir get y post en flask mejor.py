# 1. Importamos 'request' para acceder a los datos de la petición
from flask import Flask, request 
# cuidao que no es el 'requests' librería para hacer peticiones HTTP, sino 'request' que es parte de Flask para manejar las peticiones entrantes

# 2. Creamos la instancia de la aplicación
app = Flask(__name__)

# Nuestra ruta 'Hola, Mundo!' de antes
@app.route('/')
def hola_mundo():
    return '¡Bienvenido a la página principal!'

# 3. Creamos la nueva ruta para el login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 4. Comprobamos si la petición es POST
    # Si es POST, leemos el dato 'usuario' del formulario
    if request.method == 'POST':
        if request.is_json: # Si el contenido es JSON, lo leemos como JSON
            data = request.get_json()
            nombre_usuario = data.get('usuario', 'Desconocido')
            return f'<h1>¡Hola, {nombre_usuario}! Has enviado tus datos en formato JSON.</h1>'
        else: # Si no es JSON, lo leemos como formulario
            nombre_usuario = request.form['usuario']
            return f'<h1>¡Hola, {nombre_usuario}! Has enviado tus datos.</h1>'
    else: # Si no es POST, entonces es GET
        # Si es GET, mostramos el formulario para que el usuario lo rellene
        return '''
            <form method="post">
                <label>Tu nombre:</label>
                <input type="text" name="usuario">
                <input type="submit" value="Enviar">
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
