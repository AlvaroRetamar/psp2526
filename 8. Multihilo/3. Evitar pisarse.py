from threading import Thread, Lock

contador = 0
cerrojo = Lock()

def incrementar_seguro():
    global contador
    for _ in range(100000):
        # Solo uno puede entrar a la vez
        with cerrojo:
            temp = contador
            # time.sleep(0.0000001)  # Simula una operación que tarda un poco
            contador = temp + 1

if __name__ == '__main__':
    h1 = Thread(target=incrementar_seguro)
    h2 = Thread(target=incrementar_seguro)
    h1.start()
    h2.start()
    h1.join()
    h2.join()
    print(f"Contador seguro: {contador}")