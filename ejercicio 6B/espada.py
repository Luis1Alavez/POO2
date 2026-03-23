from herramienta import Herramienta

class Espada(Herramienta):
    @property
    def nombre(self) -> str:
        return "Espada"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return f"{self.nombre} de {self._material} está rota y no puede usarse"
        daño = self.calcular_daño()
        self.desgastar()
        return f"{self.nombre} de {self._material} ataca a {objetivo} (daño: {daño})"