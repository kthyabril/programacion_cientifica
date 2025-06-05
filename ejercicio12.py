def contar_impares_mayores_10(lista):
    contador = sum(1 for num in lista if num > 10 and num % 2 != 0)
    return contador

# Ejemplo de uso
numeros = [3, 15, 8, 21, 44, 11, 7, 13]
resultado = contar_impares_mayores_10(numeros)

print(f"Cantidad de números impares mayores que 10: {resultado}")