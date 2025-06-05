def encontrar_max_min(numeros):
    if not numeros: 
        return None, None
    maximo = minimo = numeros[0]
    for num in numeros:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num
    return maximo, minimo
numeros = (8, 16, 18, 21, 9, 30, 45, 14, 27, 33, 12)
maximo, minimo = encontrar_max_min(numeros)
print(f"Valor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")