from vaca import Vaca
from creeper import Creeper
from enderman import Enderman
from zombie import Zombie

# 🚀 PRUEBA tu código aquí
if __name__ == "__main__":
    mobs = [
        Vaca("Bessie", 10),
        Creeper("Explosi", 20),
        Enderman("Tall Boi", 40),
        Zombie("Walker", 25),
    ]

    for mob in mobs:
        mob.presentarse()

