class Computadora:
    def __init__(self):
        self.componentes = ["CPU", "RAM", "Disco Duro", "Tarjeta Madre", "Fuente de Poder", "Monitor", "Teclado", "Mouse"]
        self.encendida = False

    def mostrar_componentes(self):
        print("Componentes principales de la computadora:")
        for componente in self.componentes:
            print(f"- {componente}")

    def mostrar_estado(self):
        estado = "Encendida" if self.encendida else "Apagada"
        print(f"La computadora está {estado}.")

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print("La computadora se ha encendido.")
        else:
            print("La computadora ya estaba encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print("La computadora se ha apagado.")
        else:
            print("La computadora ya estaba apagada.")

# Simulación
mi_pc = Computadora()
mi_pc.mostrar_componentes()
mi_pc.mostrar_estado()

mi_pc.encender()
mi_pc.mostrar_estado()

mi_pc.apagar()
mi_pc.mostrar_estado()