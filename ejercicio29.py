valor = input("Introduce un valor (puede ser número, texto, lista, etc.): ")
tipo = type(valor).__name__
print(f"El valor ingresado es de tipo: {tipo}")