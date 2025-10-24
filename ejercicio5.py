class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    def sumar(self):
        print(f"Suma: {self.valor1 + self.valor2}")
    def restar(self):
        print(f"Resta: {self.valor1 - self.valor2}")
    def multiplicar(self):
        print(f"Multiplicación: {self.valor1 * self.valor2}")
    def dividir(self):
        if self.valor2 != 0:
            print(f"División: {self.valor1 / self.valor2}")
        else:
            print("Error: División por cero.")