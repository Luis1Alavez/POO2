from herramienta import Herramienta

class Pico(Herramienta):
    @property
    def nombre(self) -> str:
        return "Pico"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return f"{self.nombre} de {self._material} está roto y no puede usarse"
        daño = self.calcular_daño()
        self.desgastar()
        return f"{self.nombre} de {self._material} mina {objetivo} (daño: {daño})"