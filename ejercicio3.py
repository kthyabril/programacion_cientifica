def dni_valido():
    dni = input("Ingrese su número de DNI: ")
    return dni.isdigit() and 7 <= len(dni) <= 8
print(dni_valido())