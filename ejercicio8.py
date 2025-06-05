a = float(input("Ingresa a: "))
b = float(input("Ingresa b: "))
c = float(input("Ingresa c: "))
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
    area = (a * b) / 2
    perimetro = a + b + c
    print(f"El área del triángulo es {area:.1f}")
    print(f"El perímetro del triángulo es {perimetro:.1f}")
else:
    print("Los valores ingresados no corresponden a un triángulo rectángulo.")