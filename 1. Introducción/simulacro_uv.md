# SOLUCIONES - Simulacro uv

---

## Paso 1: Crear el proyecto

**Comando correcto:**
```bash
uv init simulacro
```

**Observaciones esperadas:**
- Se crea directorio "simulacro"
- Se generan archivos: pyproject.toml, README.md, hello.py, .gitignore
- Se inicializa estructura básica del proyecto
---

## Paso 2: Añadir dependencias

**Comandos correctos:**
```bash
# Para requests 2.31.0:
uv add "requests==2.31.0"

# Para pandas:
uv add pandas

# Para matplotlib:
uv add matplotlib
```

**Nota:** También es válido `uv add requests==2.31.0` (sin comillas si no hay conflictos de shell)


## Paso 3: Crear y ejecutar script

**Comando correcto:**
```bash
uv run main.py
```

**Salida esperada:**
```
✅ Todas las dependencias se importaron correctamente
Versión de pandas: 2.x.x (versión actual)
Versión de requests: 2.31.0
```

---

## Paso 4: Eliminar dependencia y sincronizar

**Comando correcto:**
```bash
uv remove matplotlib
uv sync
```