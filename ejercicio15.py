def calcular_precio_final(precio_kilo, kilos):
    if kilos <= 2:
        descuento = 0
    elif 2.01 <= kilos <= 5:
        descuento = 10
    elif 5.01 <= kilos <= 10:
        descuento = 15
    else:
        descuento = 20
    precio_total = precio_kilo * kilos
    precio_final = precio_total * (1 - descuento / 100)
    
    return precio_final
precio_kilo = float(input("Ingrese el precio por kilo de manzanas: $"))
kilos = float(input("Ingrese la cantidad de kilos comprados: "))
print(f"El cliente debe pagar: ${calcular_precio_final(precio_kilo, kilos):.2f}")