class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        if titular is None:
            raise ValueError("El titular es obligatorio.")
        self.__titular = titular
        self.__cantidad = float(cantidad)
    def get_titular(self):
        return self.__titular
    def set_titular(self, nuevo_titular):
        if nuevo_titular:
            self.__titular = nuevo_titular
    def get_cantidad(self):
        return self.__cantidad
    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: ${self.__cantidad:.2f}")
    # Ingresar dinero
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    # Retirar dinero
    def retirar(self, cantidad):
        self.__cantidad -= cantidad   
cuenta1 = Cuenta("Kathy", 100.0)
cuenta1.mostrar()
cuenta1.ingresar(50)
cuenta1.retirar(200)
cuenta1.mostrar()