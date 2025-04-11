class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_salario(self):
        return 0.0

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, Salario: {self.calcular_salario():.2f}")


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora


def main():
    empleados = [
        EmpleadoTiempoCompleto("Ana", 2500.0),
        EmpleadoPorHoras("Luis", 120, 15.5),
        Empleado("Juan")  # Base, sin salario definido
    ]

    for empleado in empleados:
        empleado.mostrar_info()


if __name__ == "__main__":
    main()