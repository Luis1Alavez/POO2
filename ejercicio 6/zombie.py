from mob import Mob

class Zombie(Mob):
    """Mob agresivo, gruñe y camina lento."""

    def hacer_sonido(self) -> str:
        return "Grrrr..."

    def comportamiento(self) -> str:
        return "agresivo"

    def moverse(self) -> str:
        return "Camina lentamente pero persigue al jugador"