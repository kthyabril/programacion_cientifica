
pies = float(input("Introduce la distancia en pies: "))
pulgadas = float(input("Introduce la distancia en pulgadas: "))
centimetros = (pies * 30.48) + (pulgadas * 2.54)
print(f"La distancia en centímetros es: {centimetros:.2f} cm")