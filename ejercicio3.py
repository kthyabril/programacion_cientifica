class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumpleaños(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tenés {self.edad} años.")