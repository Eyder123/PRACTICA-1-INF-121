# Clase base
class Animal:
    def hacerSonido(self):
        pass

    def moverse(self):
        pass

# Subclase Perro
class Perro(Animal):
    def hacerSonido(self):
        return "¡Guau guau!"

    def moverse(self):
        return "Corre rápidamente."

# Subclase Gato
class Gato(Animal):
    def hacerSonido(self):
        return "¡Miau!"

    def moverse(self):
        return "Salta ágilmente."

# Subclase Pájaro
class Pajaro(Animal):
    def hacerSonido(self):
        return "¡Pío pío!"

    def moverse(self):
        return "Vuela por el aire."


# a) Instanciar 1 Perro, 1 Gato y 1 Pájaro
animales = [
    Perro(),
    Gato(),
    Pajaro()
]

# Mostrar resultados
print("=== Sonidos de los animales ===")
for animal in animales:
    print(animal.hacerSonido())

print("\n=== Formas de moverse ===")
for animal in animales:
    print(animal.moverse())