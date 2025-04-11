class Ambiente:
    def mostrar(self):
        pass

    def cantidadMuebles(self):
        pass

class Oficina(Ambiente):
    def __init__(self, nroSillas, nroEscritorios, nroEstanterias):
        self.nroSillas = nroSillas
        self.nroEscritorios = nroEscritorios
        self.nroEstanterias = nroEstanterias

    def mostrar(self):
        print(f"Oficina - Sillas: {self.nroSillas}, Escritorios: {self.nroEscritorios}, Estanterías: {self.nroEstanterias}")

    def cantidadMuebles(self):
        return self.nroSillas + self.nroEscritorios + self.nroEstanterias

class Aula(Ambiente):
    def __init__(self, nombre, capacidad, nroPupitres):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nroPupitres = nroPupitres

    def mostrar(self):
        print(f"Aula {self.nombre} - Capacidad: {self.capacidad}, Pupitres: {self.nroPupitres}")

    def cantidadMuebles(self):
        return self.nroPupitres

class Laboratorio(Ambiente):
    def __init__(self, nombre, capacidad, nroMesas, nroSillas):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nroMesas = nroMesas
        self.nroSillas = nroSillas

    def mostrar(self):
        print(f"Laboratorio {self.nombre} - Capacidad: {self.capacidad}, Mesas: {self.nroMesas}, Sillas: {self.nroSillas}")

    def cantidadMuebles(self):
        return self.nroMesas + self.nroSillas

# a) Instanciar objetos
ambientes = [
    Oficina(3, 2, 1),
    Oficina(4, 3, 2),
    Aula("A-101", 30, 30),
    Aula("B-202", 40, 35),
    Laboratorio("Lab-Química", 25, 5, 10)
]

# b) Mostrar los datos de cada objeto
print("=== Mostrar información de los ambientes ===")
for amb in ambientes:
    amb.mostrar()

# c) Mostrar cantidad de muebles de cada ambiente
print("\n=== Cantidad total de muebles en cada ambiente ===")
for amb in ambientes:
    amb.mostrar()
    print(f"Total Muebles: {amb.cantidadMuebles()}\n")