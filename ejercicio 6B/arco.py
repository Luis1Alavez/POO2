from herramienta import Herramienta

class Arco(Herramienta):
    def __init__(self, material: str, durabilidad: int, flechas: int):
        super().__init__(material, durabilidad)
        self.flechas = flechas

    @property
    def nombre(self) -> str:
        return "Arco"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return f"{self.nombre} de {self._material} está roto y no puede disparar"
        if self.flechas == 0:
            return f"{self.nombre} de {self._material} no tiene flechas"
        daño = self.calcular_daño()
        self.desgastar()
        self.flechas -= 1
        return f"{self.nombre} de {self._material} dispara a {objetivo} (daño: {daño}, flechas: {self.flechas})"