class Coche:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad -= 5
        if self.velocidad < 0:
            self.velocidad = 0  # No puede ir a velocidad negativa

    def mostrar_velocidad(self):
        print(f"{self.marca} {self.modelo} va a {self.velocidad} km/h")

# Crear dos coches
coche1 = Coche("Toyota", "Corolla", 0)
coche2 = Coche("Ford", "Focus", 20)

# Acelerar y frenar los coches
coche1.acelerar()
coche1.frenar()

coche2.acelerar()
coche2.frenar()

# Mostrar sus velocidades
coche1.mostrar_velocidad()
coche2.mostrar_velocidad()