numeros = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
cant_pares = sum(1 for num in numeros if num % 2 == 0)
porcen_pares = round((cant_pares / len(numeros)) * 100) if numeros else 0
print(f"El porcentaje de números pares es: {porcen_pares}%")