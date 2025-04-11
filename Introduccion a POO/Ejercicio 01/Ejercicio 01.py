class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludar(self):
        print(f"Hola, soy {self.nombre} de {self.ciudad}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

persona1 = Persona("Ana", 20, "Chile")
persona2 = Persona("Luis", 16, "La Paz")
persona3 = Persona("Sofía", 25, "Argentina")

persona1.saludar()
persona2.saludar()
persona3.saludar()

# Verificar si son mayores de edad
print(f"{persona1.nombre} es mayor de edad: {persona1.es_mayor_de_edad()}")
print(f"{persona2.nombre} es mayor de edad: {persona2.es_mayor_de_edad()}")
print(f"{persona3.nombre} es mayor de edad: {persona3.es_mayor_de_edad()}")