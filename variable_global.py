#Un restaurante quiere llevar un conteo de pedidos. 
#Existe una variable global total_pedidos que guarda la cantidad 
#de pedidos hechos en el día. Cada vez que se hace un pedido, 
#la función nuevo_pedido() debe: Mostrar cuántos pedidos había antes. 
#Aumentar el total en 1. Mostrar cuántos pedidos hay.
total_pedidos = 0
def nuevo_pedido():
    global total_pedidos
    print("Pedidos antes:", total_pedidos)
    total_pedidos += 1
    print("Pedidos ahora:", total_pedidos)
nuevo_pedido()
nuevo_pedido()
nuevo_pedido()