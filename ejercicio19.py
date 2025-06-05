try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero. Solución: Usa un divisor distinto de cero.")

try:
    lista = [1, 2, 3, 4, 5]
    print(lista[10])
except IndexError:
    print("Error: Intentaste acceder a un índice que no existe en la lista. Solución: Usa índices dentro del rango de la lista.")

try:
    colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
    print(colores['blanco']) 
except KeyError:
    print("Error: La clave 'blanco' no existe en el diccionario. Solución: Verifica que la clave exista o usa .get() para evitar errores.")

try:
    resultado = 15 + "20"  
except TypeError:
    print("Error: No puedes sumar un número entero y una cadena. Solución: Convierte la cadena a entero con int('20') antes de sumarlo.")