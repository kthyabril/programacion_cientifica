entrada = input("Introduce la lista de alumnos separados por ';': ")
alumnos = entrada.split(";")  
notas = {}
for alumno in alumnos:
    nota = input(f"Ingrese la nota de {alumno.strip()}: ")
    notas[alumno.strip()] = nota  
consulta = input("Introduce el nombre del alumno para ver su nota: ")
if consulta.strip() in notas:
    print(f"La nota de {consulta.strip()} es: {notas[consulta.strip()]}")
else:
    print("El alumno no está en la lista.")