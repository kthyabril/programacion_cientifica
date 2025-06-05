def mensaje_puntos(puntos):
    if puntos > 10000:
        return "Genial, lo has hecho fenomenal."
    elif 6000 <= puntos <= 9999:
        return "Excelente."
    elif 3000 <= puntos <= 5999:
        return "Muy bien, sigue así de constante."
    elif 1000 <= puntos <= 2999:
        return "Bien, sigue aprendiendo."
    else:
        return "Es un buen comienzo, no pares."
puntos_usuario = int(input("Ingrese la cantidad de puntos acumulados: "))
print(mensaje_puntos(puntos_usuario))