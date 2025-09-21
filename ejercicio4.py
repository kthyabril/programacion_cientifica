import json

materias = {
    "Matemática": 9,
    "Ética": 8,
    "Programación": 10
}

with open("notas.json", "w") as f:
    json.dump(materias, f, indent=4)