Existe una variable global total_pedidos que guarda la cantidad de
pedidos hechos en el día. Cada vez que se hace un pedido, la
función nuevo_pedido() debe: Mostrar cuántos pedidos había
antes. Aumentar el total en 1. Mostrar cuántos pedidos hay ahora.
1. ¿Qué pasa si no usamos la palabra global dentro de la función?
2. ¿Cómo se comporta una variable local con el mismo nombre?
1. Si no usamos la palabra global dentro de la función python crea una
variable local con el mismo nombre, pero no modifica la global.
2. Esa variable solo existe dentro de la función y no afecta a la global.

