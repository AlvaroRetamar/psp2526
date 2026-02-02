from threading import Thread
import os
import time

def tarea(nombre):
    print(f"Hilo {nombre} saludando desde el proceso: {os.getpid()}")
    time.sleep(2)

if __name__ == '__main__':
    # La sintaxis es hermana de Process
    hilo1 = Thread(target=tarea, args=("A",))
    hilo2 = Thread(target=tarea, args=("B",))

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()
    print("Hilos terminados.")