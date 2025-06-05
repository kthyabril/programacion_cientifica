def fibonacci_hasta_x(x):
    secuencia = [0, 1] 
    while secuencia[-1] + secuencia[-2] <= x:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia
x = int(input("Ingrese el número límite para la sucesión de Fibonacci: "))
resultado = fibonacci_hasta_x(x)
print("Sucesión de Fibonacci hasta", x, ":", resultado)