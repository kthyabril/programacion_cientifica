import os
os.chdir("modulo_dni")  
with open("modificador.py", "w") as f:
    f.write("""
def modificar_dni(ruta_archivo, nuevo_dni):
    with open(ruta_archivo, "r") as f:
        lineas = f.readlines()
    with open(ruta_archivo, "w") as f:
        for linea in lineas:
            if linea.startswith("DNI:"):
                f.write(f"DNI: {nuevo_dni}\\n")
            else:
                f.write(linea)
""")