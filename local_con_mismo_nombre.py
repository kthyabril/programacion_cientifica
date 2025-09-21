#¿Cómo se comporta una variable local con el mismo nombre?
#esa variable solo existe dentro de la función 
# y no afecta la global.
total_pedidos = 5
def nuevo_pedido():
    total_pedidos = 0
    print("Pedidos antes (local):", total_pedidos)
    total_pedidos += 1
    print("Pedidos ahora (local):", total_pedidos)

nuevo_pedido()
print("Pedidos globales:", total_pedidos)