# 🛠️ Proyecto: Herramientas en Python (POO)

## 📖 Descripción

Este proyecto implementa **herramientas tipo Minecraft** usando **Programación Orientada a Objetos (POO)** y **clases abstractas** en Python.

Se creó la clase abstracta `Herramienta` que define:

- Propiedad abstracta `nombre`  
- Método abstracto `usar(objetivo)`  

Además, todas las herramientas comparten métodos concretos:

- `calcular_daño()`: retorna el daño según el material  
- `desgastar()`: reduce los usos restantes  
- `rota`: indica si la herramienta ya no sirve  
- `estado()`: imprime el estado con emojis y usos restantes  

---

## 🔨 Herramientas implementadas

| Clase      | Acción principal                    | Daño             | Ejemplo de salida |
|------------|-----------------------------------|-----------------|-----------------|
| Pico       | Mina bloques                        | Según material   | `Pico de diamante mina mena de diamante (daño: 6)` |
| Espada     | Ataca mobs                          | Según material   | `Espada de hierro ataca a Creeper (daño: 4)` |
| Pala       | Excava tierra, arena o grava        | Según material   | `Pala de madera excava arena (daño: 2)` |
| Arco 🔥    | Dispara flechas (Bonus)             | Según material   | `Arco de oro dispara a Esqueleto (daño: 3, flechas: 2)` |

---

## 🚀 Ejecución

1. Colocar todos los archivos en la misma carpeta:

```text
herramienta.py
pico.py
espada.py
pala.py
arco.py
main.py