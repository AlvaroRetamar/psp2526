from multiprocessing import Process, Queue
import time

def cocinero(cola):
    for i in range(15):
        item = f"Dato {i}"
        print(f"Productor: pizza {item}...")
        cola.put(item)
        time.sleep(1)

def telepizzero(cola):
    while True:
        item = cola.get() # Se bloquea aquí hasta que haya algo
        if item is None: # Señal para terminar
            break
        print(f"Consumidor: me voy a enviar la pizza {item}")
        time.sleep(10)

if __name__ == '__main__':
    mostrador = Queue()

    p1 = Process(target=cocinero, args=(mostrador,))
    p2 = Process(target=telepizzero, args=(mostrador,))

    p1.start()
    p2.start()

    p1.join()
    mostrador.put(None) # Enviamos la señal de parada al consumidor
    p2.join()

# Notas adicionales:
# Un detalle sobre el bloqueo 🛑
# Cuando un proceso llama a cola.get(), si la cola está vacía, el proceso se queda esperando (bloqueado) hasta que aparezca algo. Esto es muy útil porque no consume CPU mientras espera, pero hay que tener cuidado de no dejar procesos esperando eternamente.

# Si tenemos un proceso "Productor" muy rápido que mete 100 mensajes en la cola en un segundo, y un "Consumidor" lento que tarda 10 segundos en procesar cada mensaje... ¿qué crees que pasará con la cola mientras el consumidor trabaja?

# A. La cola se irá llenando y almacenando los mensajes.
# B. Los mensajes se perderán porque el consumidor no está listo.
# C. El productor se detendrá automáticamente hasta que el consumidor termine.





# Por defecto, en Python una Queue() no tiene un tamaño máximo definido (está limitada solo por la memoria RAM de tu computadora). Sin embargo, existe un concepto importante llamado Backpressure (contrapresión):

# Si configuras un límite, por ejemplo Queue(maxsize=10), y el productor intenta meter el mensaje número 11, el productor se detendrá (se bloqueará) automáticamente. 🛑

# Solo cuando el consumidor saque un mensaje y deje un hueco libre, el productor podrá continuar. Esto evita que un productor veloz sature toda la memoria del sistema.