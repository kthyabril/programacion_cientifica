class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    def mostrar_datos(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: ${self.cantidad}")
class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
    def mostrar_info(self):
        print("Cuenta Caja de Ahorro:")
        self.mostrar_datos()
class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes
    def calcular_interes(self):
        return self.cantidad * self.interes / 100
    def mostrar_info(self):
        interes_total = self.calcular_interes()
        print("Cuenta Plazo Fijo:")
        self.mostrar_datos()
        print(f"Plazo: {self.plazo} días")
        print(f"Interés: {self.interes}%")
        print(f"Interés generado: ${interes_total}")