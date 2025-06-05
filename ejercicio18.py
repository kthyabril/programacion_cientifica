try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero. Solución: Utiliza un divisor diferente de cero.")

try:
    lista = [1, 2, 3, 4, 5]
    print(lista[10])
except IndexError:
    print("Error: El índice está fuera del rango de la lista. Solución: Asegúrate de acceder a índices válidos dentro de la longitud de la lista.")