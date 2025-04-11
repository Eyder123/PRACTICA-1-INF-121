class Empleado:
    def __init__(self, nombre, sueldoMes):
        self.nombre = nombre
        self.sueldoMes = sueldoMes

    def sueldoTotal(self):
        return self.sueldoMes

class Cocinero(Empleado):
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora):
        super().__init__(nombre, sueldoMes)
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora

    def sueldoTotal(self):
        return self.sueldoMes + self.horasExtra * self.sueldoHora

class Mesero(Empleado):
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora, propina):
        super().__init__(nombre, sueldoMes)
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora
        self.propina = propina

    def sueldoTotal(self):
        return self.sueldoMes + self.horasExtra * self.sueldoHora + self.propina

class Administrativo(Empleado):
    def __init__(self, nombre, sueldoMes, cargo):
        super().__init__(nombre, sueldoMes)
        self.cargo = cargo

empleados = [
    Cocinero("Carlos", 1200, 10, 15.5),
    Mesero("Lucía", 1000, 5, 12.0, 50),
    Mesero("Pedro", 1100, 8, 12.5, 60),
    Administrativo("Ana", 1300, "Contadora"),
    Administrativo("Luis", 1250, "Recursos Humanos"),
]

# b) Mostrar el sueldo total de todos
print("Sueldo Total de cada empleado:")
for empleado in empleados:
    print(f"{empleado.nombre}: {empleado.sueldoTotal()}")

# c) Mostrar empleados con SueldoMes igual a X
def mostrarEmpleadosPorSueldoX(lista_empleados, x):
    print(f"\nEmpleados con sueldoMes igual a {x}:")
    for e in lista_empleados:
        if e.sueldoMes == x:
            print(e.nombre)

mostrarEmpleadosPorSueldoX(empleados, 1250)