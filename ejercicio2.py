def suma_digitos(n):
    return sum(int(d) for d in str(abs(n)))
while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    print(f"Suma de los dígitos: {suma_digitos(numero)}")