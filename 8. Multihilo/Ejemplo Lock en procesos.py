import multiprocessing
import time

def imprimir_letra(letra, repeticiones, candado):
    # Intentamos escribir una ráfaga de letras sin Lock
    for _ in range(5):
        # Creamos una cadena larga (ej. "AAAAA...")
        mensaje = letra * repeticiones
        with candado:
            print(f" INICIO {letra} -> " + mensaje + f" <- FIN {letra}\n")
        time.sleep(0.01)

if __name__ == "__main__":
    # Aumentamos el número de repeticiones para saturar el buffer
    n_repeticiones = 50000
    candado = multiprocessing.Lock()
    procesos = []
    for letra in ["A", "B", "C"]:
        p = multiprocessing.Process(target=imprimir_letra, args=(letra, n_repeticiones, candado))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()