# 🚀 Guía de Multiprocesamiento en Python

Este repositorio es una guía práctica para entender cómo ejecutar tareas en paralelo utilizando el módulo `multiprocessing`. A diferencia de los hilos (threads), los procesos en Python permiten superar el **GIL (Global Interpreter Lock)**, aprovechando al máximo todos los núcleos de tu CPU.

---

## 📖 Conceptos Clave

### 1. ¿Qué es un Proceso?

Un proceso es una instancia de un programa en ejecución. Cada proceso tiene su propio espacio de memoria. Esto significa que si cambias una variable en un proceso "hijo", no afectará al proceso "principal".

* **Aislamiento de memoria:** Seguridad total entre tareas.
* **Paralelismo real:** Ideal para tareas intensivas de cálculo (CPU Bound).

### 2. El proceso "Main"

Es el proceso principal desde donde lanzas los demás. Es vital usar el bloque `if __name__ == '__main__':` para evitar bucles infinitos de creación de procesos en Windows.

---

## 🛠️ Operadores y Funciones Principales

| Operador | Descripción |
| --- | --- |
| `Process(target, args)` | Crea un nuevo proceso hijo que ejecutará la función `target`. |
| `.start()` | Arranca la ejecución del proceso. |
| `.join()` | Bloquea el proceso principal hasta que el proceso hijo termine su tarea. |
| `daemon=True` | El proceso se ejecuta en segundo plano y se cierra automáticamente cuando el proceso principal termina. |
| `Pool()` | Crea un grupo de procesos para repartir tareas de forma automática. |

---

## 💡 Ejemplos Prácticos Realistas

### A. Procesamiento de Imágenes o Datos (Uso de `Pool`)

Si tienes 100 fotos para redimensionar, no creas 100 procesos manualmente. Usas un **Pool** (Piscina) que gestiona los trabajadores por ti.

```python
# Basado en: 5. Usando un Pool.py y 6. Y si no usamos Pool... .py
from multiprocessing import Pool

def procesar_imagen(n):
    return n * n  # Simulación de un filtro pesado

if __name__ == '__main__':
    imagenes = range(1000)
    with Pool() as pool:
        # map reparte el trabajo automáticamente entre tus núcleos
        resultados = pool.map(procesar_imagen, imagenes)
    print("Procesamiento completado.")

```

### B. Comunicación entre procesos (IPC)

Como los procesos no comparten memoria, necesitan "tuberías" o "colas" para hablar entre ellos.

1. **Queue (Colas):** Ideal para un modelo **Productor-Consumidor** (ej. una IA generando imágenes y un servidor enviándolas por email).
2. **Pipe (Tuberías):** Conexión directa entre dos puntos (ej. un sensor enviando alertas a un monitor).

```python
# Ejemplo de Alerta de Seguridad (Basado en 8. IPC - Pipe.py)
from multiprocessing import Process, Pipe

def sensor(conexion):
    conexion.send("MOVIMIENTO DETECTADO")
    print(conexion.recv()) # Espera respuesta

def monitor(conexion):
    alerta = conexion.recv()
    if alerta:
        conexion.send("ACTVANDO SIRENA")

if __name__ == '__main__':
    padre, hijo = Pipe()
    Process(target=sensor, args=(hijo,)).start()
    Process(target=monitor, args=(padre,)).start()

```

---

## ⚠️ El Problema de la Memoria (Aislamiento)

Recuerda que los procesos **no comparten variables globales**. Si intentas modificar un contador global desde un proceso hijo, el padre nunca verá el cambio.

---

## 📁 Estructura del Curso

1. **`1. Fundamentos.py`**: Tu primer "Hola Mundo" multi-proceso.
2. **`2. Aislamiento de memoria.py`**: Demostración de por qué las variables no se comparten.
3. **`3.5 Proceso daemon.py`**: Procesos que viven y mueren con el programa principal.
4. **`7. IPC - Queue.py`**: Cómo enviar datos de forma segura entre procesos y el concepto de *Backpressure*.

### 🌟 Bonus: Usando `starmap` para Múltiples Argumentos

En el mundo real, las funciones rara vez reciben un solo parámetro. Mientras que `pool.map()` solo acepta un iterable (un argumento por llamada), `pool.starmap()` permite pasar **listas de tuplas**, donde cada tupla contiene los argumentos para una ejecución.

#### Diferencia Visual

* **`map(func, [1, 2, 3])`**  Ejecuta `func(1)`, `func(2)`, `func(3)`.
* **`starmap(func, [(1, 2), (3, 4)])`**  Ejecuta `func(1, 2)`, `func(3, 4)`.

#### Ejemplo Realista: Cálculo de Áreas o Multiplicaciones

Imagina que quieres multiplicar pares de números de dos listas diferentes:

```python
# Basado en: 5. Usando un Pool.py
from multiprocessing import Pool

def multiplicar(a, b):
    return a * b

if __name__ == '__main__':
    numeros_a = [1, 2, 3]
    numeros_b = [10, 20, 30]
    
    # zip() agrupa los elementos: [(1, 10), (2, 20), (3, 30)]
    argumentos = list(zip(numeros_a, numeros_b))

    with Pool() as pool:
        # starmap "desempaqueta" cada tupla automáticamente
        resultados = pool.starmap(multiplicar, argumentos)
    
    print(f"Resultados: {resultados}") # [10, 40, 90]

```

**¿Por qué usarlo?**

* **Eficiencia:** No necesitas crear una función intermedia o "wrapper" para manejar varios parámetros.
* **Simplicidad:** Puedes combinar datos de diferentes fuentes usando `zip()` y enviarlos directamente al pool de procesos.
