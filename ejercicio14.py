hora = int(input("Ingresa la hora actual en formato 24h: "))
if hora < 12:
    print("Buenos días")
elif hora < 18:
    print("Buenas tardes")
else:
    print("Buenas noches")