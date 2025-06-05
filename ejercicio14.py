def calcular_precio_final(precio):
    if precio > 200:
        precio_final = precio * 0.8  # Aplica el descuento del 20%
    else:
        precio_final = precio  # No hay descuento
    
    return precio_final

# Solicitar el precio al usuario
precio = float(input("Ingrese el precio del producto: $"))
print(f"El cliente debe pagar: ${calcular_precio_final(precio):.2f}")