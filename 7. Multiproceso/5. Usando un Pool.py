from multiprocessing import Pool
import time

def calcular_cuadrado(n):
    time.sleep(1) # Simulamos un cálculo que tarda
    return n * n

def multiplicar(a, b):
    time.sleep(1) # Simulamos un cálculo que tarda
    return a * b

if __name__ == '__main__':
    numeros = list(range(100))
    numerosA = list(range(100))
    numerosB = list(range(100, 200))
    
    # Creamos un grupo de procesos (por defecto usa todos tus núcleos)
    with Pool() as pool:
        # # Repartimos la tarea
        # resultados = pool.map(calcular_cuadrado, numeros)
        resultados = pool.starmap(multiplicar, zip(numerosA, numerosB))
    
    print(f"Resultados: {resultados}")


# Cómo lo hacemos si la funcion tiene varios argumentos????