
precios_frutas = {
    "manzana": 2.5,
    "banana": 1.8,
    "naranja": 3.0,
    "pera": 2.2,
    "uva": 4.5
}
fruta = input("Introduce el nombre de la fruta: ").strip().lower()
if fruta in precios_frutas:
    kilos = float(input(f"Introduce la cantidad de kilos de {fruta}: "))
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kg de {fruta} es: {round(precio_total, 2)}")
else:
    print("Lo siento, la fruta ingresada no está en la lista.")