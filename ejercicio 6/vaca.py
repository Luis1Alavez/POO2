from mob import Mob

class Vaca(Mob):
    """Mob pasivo, suena 'Muuuu', camina lento."""

    def hacer_sonido(self) -> str:
        return "Muuuu"

    def comportamiento(self) -> str:
        return "pasivo"

    def moverse(self) -> str:
        return "Camina lentamente por el prado"