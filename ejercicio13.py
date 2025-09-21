import tkinter as tk
import time

def actualizar_hora():
    hora = time.strftime("%H:%M:%S")
    etiqueta.config(text=hora)
    root.after(1000, actualizar_hora)

root = tk.Tk()
etiqueta = tk.Label(root, font=("Arial", 40))
etiqueta.pack()
actualizar_hora()
root.mainloop()