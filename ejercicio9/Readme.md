# 📂 Gestión de Archivos en Python

Proyecto desarrollado en **Python** enfocado en la manipulación de archivos del sistema operativo utilizando módulos nativos como `os` y funciones de manejo de archivos.

Este ejercicio demuestra cómo Python puede interactuar directamente con el sistema de archivos para crear, editar, analizar y obtener información detallada de documentos de texto.

---

# 📌 Descripción

El proyecto simula un pequeño sistema de administración de archivos donde es posible:

- 📄 Crear archivos automáticamente
- ✍️ Escribir contenido dentro de ellos
- 📊 Analizar su tamaño real en disco
- 🔄 Convertir unidades de almacenamiento
- 🧠 Comprender el funcionamiento básico del File Handling en Python

Todo esto se realiza desde scripts simples organizados de manera modular.

---

# ⚙️ Funcionalidades Principales

## 📁 Creación de Archivos

Generación automática de archivos `.txt` utilizando Python.

```python id="f13d82"
with open("test.txt", "w") as archivo:
    archivo.write("Hola Mundo")