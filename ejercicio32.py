
caracter = input("Ingresa un carácter: ")
codigo_ascii = ord(caracter)
print(f"El código ASCII de '{caracter}' es: {codigo_ascii}")

caracter_recuperado = chr(codigo_ascii)

print(f"El carácter recuperado desde {codigo_ascii} es: '{caracter_recuperado}'")