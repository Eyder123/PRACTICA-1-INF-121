class Videojuego:
    def __init__(self, nombre="Desconocido", plataforma="Multiplataforma", cantidadJugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = cantidadJugadores

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Cantidad de Jugadores: {self.cantidadJugadores}")

    def agregarJugadores(self, cantidad=1):
        self.cantidadJugadores += cantidad
        print(f"Se han agregado {cantidad} jugador(es). Total ahora: {self.cantidadJugadores}")

videojuego1 = Videojuego("FIFA 25", "PlayStation 5", 4)
videojuego2 = Videojuego("Among Us")

# Mostrar videojuegos
print("Videojuego 1:")
videojuego1.mostrar()
print("\nVideojuego 2:")
videojuego2.mostrar()

# Agregar jugadores 
print("\nAgregando jugadores a Videojuego 1 (uno por uno):")
videojuego1.agregarJugadores()

print("\nAgregando jugadores a Videojuego 2 (cantidad personalizada):")
videojuego2.agregarJugadores(3)