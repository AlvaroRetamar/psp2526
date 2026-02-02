from threading import Thread
import time

# Variable global
contador = 0

def incrementar():
    global contador
    for _ in range(10000):
        temp = contador
        # time.sleep(0.0000001)  # Simula una operación que tarda un poco
        contador = temp + 1
    print("Hilo: He terminado de incrementar.")

if __name__ == '__main__':
    h1 = Thread(target=incrementar)
    h2 = Thread(target=incrementar)

    h1.start()
    h2.start()
    
    h1.join()
    h2.join()

    # A diferencia de los procesos, aquí el valor SÍ cambia
    # Pero cuidado: ¡aquí introduces el concepto de RACE CONDITION!
    print(f"Principal: El valor final del contador es {contador}")