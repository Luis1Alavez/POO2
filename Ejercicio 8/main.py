from Competidor import Competidor
from Observador import Observador


carlos = Competidor("Carlos Méndez", "21100123", "avanzado", "Team Overflow")
carlos.mostrar_perfil()
carlos.ganar_puntos(50)
carlos.perder_puntos(20)

print("\n")


ana = Observador("Ana Torres", "21100456", "principiante")
ana.ganar_puntos(0) 
ana.ver_partida()
ana.ver_partida()
ana.mostrar_perfil()