from tkinter import Menu
Menu()
if __name__ == "__main__":
    def main_menu():
        inventario = {}
        while True:
            print("\n1. Cargar producto")
            print("2. Listar productos")
            print("3. Buscar producto")
            print("4. Calcular valor total")
            print("5. Salir")
            try:
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    cargar_producto(inventario)
                elif opcion == "2":
                    lista(inventario)
                elif opcion == "3":
                    buscar(inventario)
                elif opcion == "4":
                    valor_total(inventario)
                elif opcion == "5":
                    print("Gracias por usar el sistema de gestión de inventario. ¡Hasta luego!")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.\n")
            except Exception as e:
                print(f"Error: {e}. Intente nuevamente.\n")
    main_menu()
    def cargar_producto(inventario):
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre in inventario:
            print("El producto ya existe. Actualizando cantidad y precio.")
        try:
            precio = float(input("Ingrese el precio unitario: "))
            cantidad = int(input("Ingrese la cantidad disponible: "))
            inventario[nombre] = {"precio": precio, "cantidad": cantidad}
            print(f"Producto '{nombre}' agregado correctamente.")
        except ValueError:
            print("Error: Ingrese valores válidos para precio y cantidad.")

    def lista(inventario):
        if not inventario:
            print("No hay productos en el inventario.")
            return
        print("\nInventario de productos:")
        for nombre, datos in inventario.items():
            print(f"Nombre: {nombre}, Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")

    def buscar(inventario):
        nombre = input("Ingrese el nombre del producto a buscar: ").strip()
        if nombre in inventario:
            datos = inventario[nombre]
            print(f"Producto encontrado - Nombre: {nombre}, Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")
        else:
            print("Producto no encontrado.")

    def valor_total(inventario):
        total = sum(datos['precio'] * datos['cantidad'] for datos in inventario.values())
        print(f"El valor total del inventario es: {total}")