class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena.")
    def get_nombre(self):
        return self.nombre
    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            raise ValueError("La edad debe ser un número entero no negativo.")
    def get_edad(self):
        return self.edad
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) >= 7:
            self.dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena válida.")
    def get_dni(self):
        return self.dni
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")
    def es_mayor_de_edad(self):
        return self.edad >= 18