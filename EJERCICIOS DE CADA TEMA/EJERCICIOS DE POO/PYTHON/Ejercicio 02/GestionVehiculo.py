class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Vehículo: {self.marca} {self.modelo}")


class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        print(f"Auto: {self.marca} {self.modelo} - Puertas: {self.puertas}")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, tiene_sidecar):
        super().__init__(marca, modelo)
        self.tiene_sidecar = tiene_sidecar

    def mostrar_info(self):
        sidecar_str = "Sí" if self.tiene_sidecar else "No"
        print(f"Moto: {self.marca} {self.modelo} - Sidecar: {sidecar_str}")


def main():
    v1 = Auto("Toyota", "Corolla", 4)
    v2 = Moto("Yamaha", "MT-07", False)

    v1.mostrar_info()
    v2.mostrar_info()


if __name__ == "__main__":
    main()