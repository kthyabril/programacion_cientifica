nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu número de teléfono: ")
usuario = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")