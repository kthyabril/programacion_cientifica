import json
with open("notas.json", "r") as f:
    datos = json.load(f)
    print(datos)