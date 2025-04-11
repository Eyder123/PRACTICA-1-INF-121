class Aplicacion:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano  # en MB

class Celular:
    def __init__(self):
        self.espacio_total = 1024  # en MB
        self.max_apps = 20
        self.bateria = 100  # porcentaje
        self.aplicaciones = []

    def instalar_app(self, app):
        if len(self.aplicaciones) < self.max_apps and self.espacio_disponible() >= app.tamano:
            self.aplicaciones.append(app)
            print(f"Aplicación '{app.nombre}' instalada correctamente.")
        else:
            print("No se pudo instalar la aplicación. Espacio o límite de aplicaciones excedido.")

    def espacio_disponible(self):
        return self.espacio_total - sum(app.tamano for app in self.aplicaciones)

    def usar_app(self, nombre_app, minutos):
        if self.bateria <= 0:
            print("Celular apagado. No se puede usar ninguna aplicación.")
            return

        app = next((app for app in self.aplicaciones if app.nombre == nombre_app), None)
        if app is None:
            print("Aplicación no encontrada.")
            return

        if app.tamano > 250:
            consumo_por_10_min = 5
        elif app.tamano > 100:
            consumo_por_10_min = 2
        else:
            consumo_por_10_min = 1

        periodos_de_10_min = minutos // 10
        consumo_total = consumo_por_10_min * periodos_de_10_min

        self.bateria -= consumo_total
        if self.bateria <= 0:
            self.bateria = 0
            print("La batería se ha agotado. Celular apagado.")
        else:
            print(f"Usaste la app '{app.nombre}' por {minutos} minutos. Batería restante: {self.bateria}%")

    def mostrar_bateria(self):
        print(f"Batería restante: {self.bateria}%")

cel = Celular()
app1 = Aplicacion("Facebook", 150)
app2 = Aplicacion("Juego Pesado", 300)
app3 = Aplicacion("Notas", 50)

cel.instalar_app(app1)
cel.instalar_app(app2)
cel.instalar_app(app3)

cel.usar_app("Facebook", 30)
cel.mostrar_bateria()
cel.usar_app("Juego Pesado", 60)
cel.mostrar_bateria()
cel.usar_app("Notas", 100)
cel.mostrar_bateria()