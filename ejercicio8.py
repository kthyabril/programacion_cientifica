numeros_ganadores = []
cantidad_numeros = 6  
print("Introduce los números ganadores de la lotería primitiva:")
for i in range(cantidad_numeros):
    numero = int(input(f"Número {i+1}: "))
    numeros_ganadores.append(numero)
numeros_ganadores.sort()
print("Los números ganadores ordenados son:", numeros_ganadores)