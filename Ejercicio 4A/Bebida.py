from Platillo import Platillo

class Bebida(Platillo):
    def __init__(self, nombre, precio, temperatura):
        super().__init__(nombre, precio)
        self.temperatura = temperatura

    def tipo(self):
        if self.temperatura.lower() == "fría":
            return "Bebida fría"
        elif self.temperatura.lower() == "caliente":
            return "Bebida caliente"
        else:
            return "Tipo desconocido"

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Tipo: {self.tipo}")