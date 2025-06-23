def generar_identificador(nombre, dni):
    partes = nombre.strip().split()
    if len(partes) < 2:
        return None
    inicial = partes[0][0].upper()
    apellido = partes[-1].capitalize()
    ultimos_digitos_dni = dni[-3:]
    return f"{inicial}{apellido}{ultimos_digitos_dni}"

while True:
    nombre = input("Ingrese nombre completo del socio (vacío para terminar): ").strip()
    if nombre == "":
        break
    dni = input("Ingrese número de DNI: ").strip()
    if not dni.isdigit() or len(dni) < 3:
        print("DNI inválido. Intente nuevamente.")
        continue
    identificador = generar_identificador(nombre, dni)
    if identificador:
        print(f"Identificador del socio: {identificador}")
    else:
        print("Debe ingresar al menos nombre y apellido.")