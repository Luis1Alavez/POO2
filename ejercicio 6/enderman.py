from mob import Mob

class Enderman(Mob):
    """Mob neutral, sonido distorsionado, se teletransporta."""

    def hacer_sonido(self) -> str:
        return "Sonido distorsionado y extraño"

    def comportamiento(self) -> str:
        return "neutral"

    def moverse(self) -> str:
        return "Se teletransporta de un lugar a otro"