# 🏰 Proyecto: Mobs en Python (POO)

## 📖 Descripción

Este proyecto implementa **mobs de un juego tipo Minecraft** usando **Programación Orientada a Objetos (POO)** y **clases abstractas** en Python.  

Se creó una **clase abstracta `Mob`** que define los métodos esenciales que todos los mobs deben implementar:  

- `hacer_sonido()`: retorna el sonido característico del mob  
- `comportamiento()`: indica si el mob es pasivo, agresivo o neutral  
- `moverse()`: describe cómo se mueve el mob  

Luego, se implementaron **subclases concretas** que heredan de `Mob`:

| Clase      | Comportamiento | Sonido                  | Movimiento                              |
|------------|----------------|------------------------|----------------------------------------|
| Vaca       | pasivo         | Muuuu                  | Camina lentamente por el prado         |
| Creeper    | agresivo       | ...Ssssss              | Corre directamente hacia el jugador    |
| Enderman   | neutral        | Sonido distorsionado    | Se teletransporta                       |
| Zombie 💎 | agresivo       | Grrrr...               | Camina lentamente persiguiendo jugador |

Cada mob puede **presentarse** con un método `presentarse()` que imprime sus características con emojis para mayor claridad visual.  

---

## 🚀 Ejecución

1. Colocar todos los archivos en la misma carpeta:  
   `mob.py`, `vaca.py`, `creeper.py`, `enderman.py`, `zombie.py`, `main.py`  

2. Ejecutar desde la terminal:

```bash
python main.py