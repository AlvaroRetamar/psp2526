from multiprocessing import Process, Pool, Queue

def calcular_cuadrado(n):
    return n * n

# --- Alternativa A: Usando Process (Manual) ---
def ejemplo_process(datos):
    procesos = []
    # Necesitamos una herramienta extra (Queue) para "recoger" los resultados
    cola_resultados = Queue()

    def tarea_con_cola(n, q):
        resultado = calcular_cuadrado(n)
        q.put(resultado) # Metemos el resultado en la "tubería"

    for numero in datos:
        p = Process(target=tarea_con_cola, args=(numero, cola_resultados))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    # Extraemos los resultados de la cola
    resultados = [cola_resultados.get() for _ in procesos]
    return resultados

# --- Alternativa B: Usando Pool (Automático) ---
def ejemplo_pool(datos):
    with Pool() as pool:
        # Internamente hace todo: crea procesos, los gestiona y devuelve la lista
        return pool.map(calcular_cuadrado, datos)

if __name__ == '__main__':
    numeros = [1, 2, 3, 4]
    
    print("Resultados con Process:", ejemplo_process(numeros))
    print("Resultados con Pool:", ejemplo_pool(numeros))