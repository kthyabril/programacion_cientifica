# Sistema escolar para el IPET 1308
Ipet = {
    "Analista de Sistemas de Computación": {
        "precio": 40000,
        "profesores": "Ing. De Sosa Héctor",
        "contacto": "info@ipet.com.ar",
        "alumnos": ["Katherine", "Carlos", "Luciana", "Vanina"],
        "evaluacion_promedio": 8.5
    },
    "Secretariado Administrativo": {
        "precio": 40000,
        "profesor": "Prof. Gómez",
        "contacto": "info@ipet.com.ar",
        "alumnos": ["Ana", "Javier", "Matías"],
        "evaluacion_promedio": 7.8
    },
    "Analista Programador": {
        "precio": 40000,
        "profesor": "Reis Luis",
        "contacto": "info@ipet.com.ar",
        "alumnos": ["Katherine", "Carlos", "Luciana", "Vanina"],
        "evaluacion_promedio": 9.2
    }
}
carrera = input("Ingrese el nombre de la carrera: ").strip()
if carrera in Ipet:
    datos = Ipet[carrera]
    print(f"\nCarrera: {carrera}")
    print(f"Precio: {datos['precio']}")
    print(f"Profesor: {datos['profesor']}")
    print(f"Contacto: {datos['contacto']}")
    print(f"Lista de alumnos: {', '.join(datos['alumnos'])}")
    print(f"Evaluación promedio: {datos['evaluacion_promedio']}")
else:
    print("La carrera ingresada no está registrada.")