from mob import Mob

class Creeper(Mob):
    """Mob agresivo, suena '...Ssssss', corre hacia el jugador."""

    def hacer_sonido(self) -> str:
        return "...Ssssss"

    def comportamiento(self) -> str:
        return "agresivo"

    def moverse(self) -> str:
        return "Corre directamente hacia el jugador"