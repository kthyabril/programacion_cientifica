import os
import shutil
os.mkdir("carpeta_prueba")
with open("carpeta_prueba/modulo.py", "w") as f:
    f.write("# módulo de prueba")
try:
    os.rmdir("carpeta_prueba")  
except OSError:
    print("No se puede eliminar: la carpeta contiene archivos.")
shutil.rmtree("carpeta_prueba") 