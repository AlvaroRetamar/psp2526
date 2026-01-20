from multiprocessing import Process, Queue
import time

def productor(cola):
    for i in range(3):
        item = f"Dato {i}"
        print(f"Productor: Enviando {item}...")
        cola.put(item)
        time.sleep(1)

def consumidor(cola):
    while True:
        item = cola.get() # Se bloquea aquí hasta que haya algo
        if item is None: # Señal para terminar
            break
        print(f"Consumidor: Recibido {item}")

if __name__ == '__main__':
    mi_cola = Queue()

    p1 = Process(target=productor, args=(mi_cola,))
    p2 = Process(target=consumidor, args=(mi_cola,))

    p1.start()
    p2.start()

    p1.join()
    mi_cola.put(None) # Enviamos la señal de parada al consumidor
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