class Figura:
    def calcular_area(self):
        return 0

    def mostrar(self):
        print("Soy una figura.")

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def mostrar(self):
        print(f"Cuadrado. Lado: {self.lado}, Área: {self.calcular_area()}")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def mostrar(self):
        print(f"Rectángulo. Base: {self.base}, Altura: {self.altura}, Área: {self.calcular_area()}")

f1 = Cuadrado(4)
f2 = Rectangulo(5, 3)

f1.mostrar()
f2.mostrar()