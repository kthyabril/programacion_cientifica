class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0
    def depositar(self, monto):
        self.cantidad += monto
    def extraer(self, monto):
        self.cantidad -= monto
    def mostrar_total(self):
        print(f"{self.nombre} tiene ${self.cantidad}")
class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Ana")
        self.cliente2 = Cliente("Kathy")
        self.cliente3 = Cliente("Abril")
    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(1500)
        self.cliente3.depositar(2000)
        self.cliente2.extraer(500)
    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad
        print(f"Total depositado en el banco: ${total}")