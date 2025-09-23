# Examen Práctico de Git
## Organización de Fiesta de Fin de Curso

### 📋 Información General

**Duración:** 50 minutos  
**Puntuación total:** 100 puntos  
**Herramientas permitidas:** Cualquier interfaz de Git (línea de comandos, Visual Studio Code, GitHub Desktop, etc.)

### 🎯 Objetivos
Este examen evaluará tu capacidad para usar Git de manera práctica en un proyecto real. Demostrarás que sabes:
- Crear repositorios y hacer commits
- Trabajar con ramas (branches)
- Fusionar cambios (merge)
- Subir tu trabajo a GitHub

### 🎉 Contexto del Ejercicio
Eres parte del comité organizador de la fiesta de fin de curso. Usarás Git para gestionar toda la documentación y tareas del evento. Al final tendrás un repositorio completo con toda la planificación.

---

## 📝 Ejercicio Práctico

### Parte 1: Configuración inicial del proyecto

1. **Crear repositorio local**
   - Nombre: `fiesta-fin-curso-[tu-nombre]` (sustituye [tu-nombre] por tu nombre real)

2. **Crear archivo README**
   - Archivo: `README.txt`
   - Contenido:
     - Tu nombre como organizador
     - Fecha de hoy
     - Descripción: "Repositorio para organizar la fiesta de fin de curso"

3. **Primer commit**
   - Mensaje: `"Iniciar proyecto de organización de fiesta"`

### Parte 2: Planificación básica (20 puntos)

4. **Lista de invitados inicial**
   - Crear `invitados.txt` con 5 nombres de compañeros de clase
   - Commit con mensaje: `"Crear lista inicial de invitados"`

5. **Ampliar invitados y crear presupuesto**
   - Añadir 3 invitados más a `invitados.txt`
   - Crear `presupuesto.txt` con:
     ```
     Decoración: 50€
     Comida: 100€
     Bebidas: 30€
     Música: 20€
     ```
   - Hacer un commit para cada cambio
   - Mensaje: `"Actualizar invitados"`
   - Mensaje: `"Crear presupuesto"`

6. **Mejorar documentación**
   - Modificar `README.txt` añadiendo:
     - Fecha de la fiesta (invéntala)
     - Lugar de la fiesta (invéntalo)
   - Commit con mensaje: `"Añadir detalles básicos del evento"`

### Parte 3: Trabajando en paralelo - Planificación de música (30 puntos)

7. **Crear y cambiar a nueva rama**
   - Nombre de la rama: `playlist-musica`

8. **Crear playlist inicial**
   - Crear `canciones.txt` con 5 canciones que pondrías en la fiesta
   - Commit con mensaje: `"Crear playlist inicial"`

9. **Ampliar contenido musical**
   - Añadir 3 canciones más a `canciones.txt`
   - Crear `equipos.txt` con:
     ```
     Altavoces: Necesarios
     Micrófono: Opcional
     Luces: Necesarias
     ```
   - Hacer UN commit para cada cambio
   - Mensaje: `"Ampliar playlist"`
   - Mensaje: `"Definir equipos de música"`

10. **Volver a rama principal y trabajar en decoración**
    - Cambiar a la rama principal (`main` o `master`)
    - Crear `decoracion.txt` con:
      ```
      Globos: 20 unidades
      Guirnaldas: 5 metros
      Carteles: 3 unidades
      ```
    - Commit con mensaje: `"Planificar decoración del evento"`

### Parte 4: Integrar el trabajo (25 puntos)

11. **Fusionar ramas**
    - Desde la rama principal, fusionar la rama `playlist-musica`

12. **Limpiar ramas**
    - Eliminar la rama `playlist-musica` después del merge

13. **Crear tareas pendientes**
    - Crear `tareas-pendientes.txt` con:
      ```
      - Comprar decoración
      - Reservar lugar
      - Confirmar asistencia
      - Preparar música
      - Organizar limpieza post-fiesta
      ```
    - Commit con mensaje: `"Crear lista de tareas pendientes"`

### Parte 5: Publicación del proyecto (15 puntos)

14. **Subir a GitHub**
    - Crear repositorio público en GitHub: `fiesta-fin-curso-[tu-nombre]`
    - Conectar repositorio local con GitHub
    - Subir todo el trabajo

15. **Entregar**
    - **Compartir el enlace del repositorio de GitHub al finalizar**

---

## ✅ Verificación Final

Al terminar, tu repositorio debe contener estos archivos:
- `README.txt` (información del proyecto y evento)
- `invitados.txt` (lista completa de invitados)
- `presupuesto.txt` (desglose económico)
- `decoracion.txt` (elementos decorativos)
- `canciones.txt` (playlist de la fiesta)
- `equipos.txt` (equipamiento musical)
- `tareas-pendientes.txt` (tareas por hacer)

## 🎯 Criterios de Evaluación

- **Commits correctos**: Mensajes claros y commits en momentos lógicos
- **Uso de ramas**: Creación, trabajo independiente y merge correcto
- **Estructura de archivos**: Todos los archivos solicitados con contenido apropiado
- **Repositorio GitHub**: Subido correctamente y accesible
- **Historial limpio**: Se puede seguir el progreso del trabajo

## 📚 Recordatorios

- **Puedes usar cualquier herramienta Git que prefieras**
- **Los archivos solo deben contener texto simple**
- **Cada commit debe tener un mensaje descriptivo**
- **¡No olvides compartir el enlace de GitHub al terminar!**

---

**¡Buena suerte! 🎉**