class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad
class Estudiante:
    def __init__(self, nombre, edad, universidad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Especialidad: {self.carrera.especialidad}")
        print(f"Universidad: {self.universidad.nombre}")