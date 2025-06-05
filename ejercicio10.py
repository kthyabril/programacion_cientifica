numeros = [8, 16, 18, 21, 9, 30, 45, 14, 27, 33, 12]
multiples = [num for num in numeros if num % 3 == 0 and num > 15]
print(f"Cantidad de números múltiplos de 3 y mayores que 15: {len(multiples)}")