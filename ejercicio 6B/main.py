from pico import Pico
from espada import Espada
from pala import Pala
from arco import Arco

if __name__ == "__main__":
    herramientas = [
        Pico("diamante", 5),
        Espada("hierro", 3),
        Pala("madera", 2),
        Arco("oro", 4, 3),  # bonus
    ]
    objetivos = ["mena de diamante", "Creeper", "arena", "Esqueleto"]

    for h, obj in zip(herramientas, objetivos):
        print(h.usar(obj))
        h.estado()
        print()