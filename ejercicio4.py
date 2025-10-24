class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor es: {mayor}")
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Es un triángulo equilátero.")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("Es un triángulo isósceles.")
        else:
            print("Es un triángulo escaleno.")