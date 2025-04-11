# Clase base
class Bloque:
    def colocar(self, orientacion):
        print(f"Bloque colocado en la orientación: {orientacion}")

    def accion(self):
        pass

    def romper(self):
        pass


# Clase BloqueCofre
class BloqueCofre(Bloque):
    def __init__(self, capacidad, resistencia, tipo):
        self.capacidad = capacidad
        self.resistencia = resistencia
        self.tipo = tipo

    def accion(self):
        print(f"Abriendo el cofre tipo '{self.tipo}' con capacidad de {self.capacidad} items.")

    def romper(self):
        print(f"Has roto un cofre tipo '{self.tipo}'. Los objetos caen al suelo.")


# Clase BloqueTnt
class BloqueTnt(Bloque):
    def __init__(self, tipo, danio):
        self.tipo = tipo
        self.danio = danio

    def accion(self):
        print(f"Activando TNT tipo '{self.tipo}'... ¡Corre!")

    def romper(self):
        print(f"Rompiste una TNT tipo '{self.tipo}'... ¡Explosión con daño de {self.danio}!")


# Clase BloqueHorno
class BloqueHorno(Bloque):
    def __init__(self, color, capacidadComida):
        self.color = color
        self.capacidadComida = capacidadComida

    def accion(self):
        print(f"Usando horno color '{self.color}' para cocinar {self.capacidadComida} unidades de comida.")

    def romper(self):
        print(f"El horno '{self.color}' se ha roto. Los alimentos quedan crudos.")


# a) Crear e instanciar al menos 2 bloques de cada tipo
bloques = [
    BloqueCofre(30, 10, "Madera"),
    BloqueCofre(50, 15, "Hierro"),
    BloqueTnt("Explosiva", 100),
    BloqueTnt("Controlada", 50),
    BloqueHorno("Negro", 4),
    BloqueHorno("Gris", 6)
]

# b) Ejecutar acción
print("=== Acciones de los bloques ===")
for bloque in bloques:
    bloque.accion()

# c) Colocar en diferentes orientaciones
print("\n=== Colocando bloques ===")
orientaciones = ["en el suelo", "en la pared", "en el techo"]
for i, bloque in enumerate(bloques):
    bloque.colocar(orientaciones[i % len(orientaciones)])

# d) Romper bloques
print("\n=== Rompiendo bloques ===")
for bloque in bloques:
    bloque.romper()