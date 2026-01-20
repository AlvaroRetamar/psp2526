# Ejercicio Práctico: Optimizando el Procesamiento de Datos con Multiproceso en Python

## 🎯 Objetivo

El objetivo de esta práctica es comparar el rendimiento de un script de procesamiento de datos secuencial (un solo núcleo) frente a una implementación paralela utilizando el módulo `multiprocessing` de Python.

---

## 📂 Archivos del Proyecto

Cuentas con los siguientes archivos base:

1. **`preparar_datos.py`**: Genera 150 archivos de texto con contenido aleatorio en una carpeta llamada `./datos_ejercicio`.
2. **`procesador.py`**: Contiene la función `analizar_archivo()`. Esta función tiene un retraso artificial de 0.5 segundos para simular una carga de trabajo pesada o una lectura lenta de disco.
3. **`main_sin_multiproceso.py`**: Plantilla para el código secuencial.
4. **`main_con_multiproceso.py`**: Plantilla para el código en paralelo.

---

## 🛠️ Instrucciones

### Paso 1: Generación de datos

Ejecuta el script de preparación para crear el entorno de pruebas

### Paso 2: Implementación Secuencial

Abre el archivo `main_sin_multiproceso.py`. Debes completar la sección indicada utilizando un bucle `for` tradicional o una *list comprehension* para procesar cada archivo de la lista uno por uno.

**Requisito:** Guarda los diccionarios retornados por `analizar_archivo` en una lista llamada `resultados`.

### Paso 3: Implementación con Multiproceso

Abre el archivo `main_con_multiproceso.py`. En este caso, debes utilizar varios procesos para agilizar los cálculos.

Al igual que en el paso anterior, el resultado debe guardarse en la variable `resultados`.

---

## 📊 Comparativa de Rendimiento

Una vez completados los scripts, ejecuta ambos y completa la siguiente tabla con tus resultados:

|Método|Tiempo Total (segundos)|Observaciones|
|---|---|---|
|**Secuencial**|||
|**Multiproceso**|||

---

## 💡 Preguntas de Reflexión

1. **¿Por qué el tiempo en multiproceso no es simplemente "tiempo secuencial / número de núcleos"?** (Pista: investiga sobre el *overhead* o sobrecarga de creación de procesos).
2. **¿Qué sucede con el uso de la CPU en el Administrador de Tareas (o Monitor de Actividad) durante la ejecución de cada script?**
3. Si eliminamos el `time.sleep(0.5)` del procesador, **¿seguirá valiendo la pena usar multiproceso para archivos muy pequeños?**
