class Animal:
    def hacer_sonido(self):
        print("Sonido genérico de animal")


class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau!")


class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau!")


def main():
    animales = [
        Perro(),
        Gato(),
        Animal()
    ]

    for animal in animales:
        animal.hacer_sonido()


if __name__ == "__main__":
    main()