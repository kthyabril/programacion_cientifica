datos = "7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;"
promedios = {}
registros = datos.split(";;") 
for registro in registros:
    if registro:  
        notas_texto, nombre = registro.split("#")
        notas = list(map(float, notas_texto.split(","))) 
        promedio = sum(notas) / len(notas) 
        promedios[nombre] = round(promedio, 2) 
print(promedios)