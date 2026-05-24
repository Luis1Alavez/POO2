class Jugador:
    def __init__(self, nombre, num_control, nivel):
        self.nombre = nombre
        self.num_control = num_control
        self.nivel = nivel
        self.puntos = 0

    def ganar_puntos(self, puntos):
        self.puntos += puntos
        print   (f"{self.nombre} ganó {puntos} puntos. Total: {self.puntos}")

    def perder_puntos(self, puntos):
        self.puntos -= puntos
        print   (f"{self.nombre} perdió {puntos} puntos. Total: {self.puntos}") 

        if self.puntos < 0:
            self.puntos = 0
            
    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de control: {self.num_control}")
        print(f"Nivel: {self.nivel}")
        print(f"Puntos: {self.puntos}")