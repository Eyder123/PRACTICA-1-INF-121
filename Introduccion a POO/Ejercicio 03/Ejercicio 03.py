class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def calcular_promedio(self):
        return (self.nota_1 + self.nota_2) / 2

    def aprobo(self):
        return self.calcular_promedio() >= 6

est1 = Estudiante("Carlos", 7.5, 6.0)
est2 = Estudiante("Lucía", 5.0, 4.5)
est3 = Estudiante("Martín", 8.0, 9.0)

for est in [est1, est2, est3]:
    promedio = est.calcular_promedio()
    print(f"{est.nombre}: Promedio = {promedio:.2f} - Aprobó: {est.aprobo()}")