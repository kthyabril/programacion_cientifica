#¿Qué pasa si no usamos la palabra global dentro de la función?

#Python crea una variable local con el mismo nombre, 
# pero no modifica la global.
total_pedidos = 0
def nuevo_pedido():
    print("Pedidos antes:", total_pedidos)  # ❌ Error: variable referenciada antes de ser asignada
    total_pedidos += 1
    print("Pedidos ahora:", total_pedidos)