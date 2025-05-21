segundos = int(input("Introduce la cantidad de segundos: "))
minutos = segundos // 60
segundos_restantes = segundos % 60
print(f"{segundos} segundos son {minutos} minutos y {segundos_restantes} segundos.")
