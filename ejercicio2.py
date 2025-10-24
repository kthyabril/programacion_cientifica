class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 6:
            print("¡Aprobado!")
        else:
            print("Desaprobado.")