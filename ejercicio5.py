import json
with open("notas.json", "w") as f:
    json.dump({"Historia": 7}, f)