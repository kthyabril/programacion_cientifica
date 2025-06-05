def suma_serie(n):
    suma = 0
    for i in range(1, n+1):
        suma += 1/i
    return suma
n = int(input("Ingrese el número de términos: "))
print(f"La suma de los primeros {n} términos es: {suma_serie(n):.6f}")