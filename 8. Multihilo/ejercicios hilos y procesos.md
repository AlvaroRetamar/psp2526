# Ejercicios para practicar

## 1. El Simulador de Renderizado

Este código demuestra la diferencia de rendimiento entre el procesamiento secuencial y el paralelo.

```python
import multiprocessing
import time

def calcular_primos(n):
    # Tarea intensiva de CPU: contar primos hasta n
    count = 0
    for i in range(2, n):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            count += 1
    return count

if __name__ == "__main__":
    tareas = [100000] * 20  # 20 tareas pesadas
    
    # Secuencial
    inicio = time.time()
    for t in tareas:
        calcular_primos(t)
    print(f"Secuencial: {time.time() - inicio:.2f} segundos")

    # Multiprocesamiento
    inicio = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(calcular_primos, tareas)
    print(f"Paralelo (Pool): {time.time() - inicio:.2f} segundos")

```

---

## 2. El Almacén Logístico

Aquí usamos una `Queue` para comunicar procesos y un `Lock` para que los mensajes en consola no se pisen.

```python
import multiprocessing
import time
import random

def operario(id, cola, candado):
    while True:
        paquete = cola.get()
        if paquete is None: # Señal de salida
            break
        
        # Simular procesamiento
        time.sleep(random.random())
        
        with candado:
            print(f"Operario {id} procesó paquete {paquete}")

if __name__ == "__main__":
    cola_tareas = multiprocessing.Queue()
    candado = multiprocessing.Lock()
    procesos = []

    # Crear 3 operarios
    for i in range(3):
        p = multiprocessing.Process(target=operario, args=(i, cola_tareas, candado))
        p.start()
        procesos.append(p)

    # El Productor genera 10 paquetes
    for i in range(10):
        cola_tareas.put(f"REF-{i}")

    # Enviar señales de parada
    for _ in range(3):
        cola_tareas.put(None)

    for p in procesos:
        p.join()

```

---

## 3. Web Scraper Veloz

Usamos hilos porque el cuello de botella es la espera de red (I/O Bound).

```python
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def check_url(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return f"{url}: {response.getcode()}"
    except Exception as e:
        return f"{url}: Error"

urls = ["https://www.google.com", "https://www.python.org", "https://www.github.com"] * 5

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        resultados = list(executor.map(check_url, urls))
    
    for r in resultados:
        print(r)

```

---

## 4. La Cuenta Bancaria (Race Condition)

Este ejercicio es vital para entender por qué necesitamos `Locks` incluso en hilos de Python.

```python
import threading
import time

saldo = 100
lock = threading.Lock()

def retirar_dinero():
    global saldo
    # Leer el saldo
    temp = saldo
    time.sleep(0.01) # Forzamos el cambio de contexto
    # Escribir el saldo
    saldo = temp - 10

def retirar_con_seguridad():
    global saldo
    with lock:
        temp = saldo
        time.sleep(0.01)
        saldo = temp - 10

if __name__ == "__main__":
    hilos = []
    # Prueba SIN lock (fallará, el saldo no será 0)
    for _ in range(10):
        h = threading.Thread(target=retirar_dinero)
        h.start()
        hilos.append(h)
    
    for h in hilos: h.join()
    print(f"Saldo final sin Lock: {saldo}") # Resultado impredecible

```
