agenda = {
    "lunes": [],
    "martes": [],
    "miércoles": [],
    "jueves": [],
    "viernes": [],
    "sábado": [],
    "domingo": []
}
while True:
    dia = input("Dime el día de la semana (o escribe 'salir' para finalizar): ").strip().lower()
    
    if dia == "salir":
        print("Agenda cerrada.")
        break
    if dia in agenda:
        tareas = agenda[dia]
        if tareas:
            print(f"Tienes {len(tareas)} tareas pendientes:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
        else:
            print("Tienes 0 tareas pendientes.")
        nueva_tarea = input("¿Qué anotamos? (Deja vacío si no quieres agregar nada): ").strip()
        if nueva_tarea:
            agenda[dia].append(nueva_tarea)
            print(f"Tarea añadida: {nueva_tarea}")
    else:
        print("Día inválido. Intenta de nuevo.")