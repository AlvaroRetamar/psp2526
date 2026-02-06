# usando el modulo requests, sacar lo datos de un pokemon
import requests
url_base = "https://pokeapi.co/api/v2/pokemon/"

pokemoncillo = requests.get(url_base+'150').json()
print(pokemoncillo['name'])
for i in range(len(pokemoncillo['stats'])):
    print(f'indice {i} estadistica: {pokemoncillo['stats'][i]['stat']['name']}')

# nombre, ataque, defensa y velocidad

# crear una clase pokemon con los atributos ataque, defensa y velocidad

# descargar los datos de 128 pokemon de la pokeapi (https://pokeapi.co/) usando hilos y guardarlos en objetos de tipo pokemon

# usando procesos, hacer combates entre los pokemon descargados y mostrar el ganador de cada combate
# para cada combate, se eligen dos pokemon al azar, el mas rapido es el atacante, si la velocidad es igual, es atacante el tenga mas ataque
# si el ataque es mayor que la defensa gana el atacante, si la defensa es igual o superior, gana el defensor