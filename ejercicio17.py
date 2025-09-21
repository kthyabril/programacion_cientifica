def guardar_contacto(nombre, telefono):
    with open("agenda.txt", "a") as f:
        f.write(f"{nombre},{telefono}\n")