import tkinter as tk
root = tk.Tk()
root.title("Calculadora de Katherine")
root.geometry("300x400")  # Tamaño de ventana

btn_num = tk.Button(root, text="1", bg="lightblue", fg="black")
btn_num.pack()
def cm_a_metros(cm):
    return cm / 100

def ha_a_m2(ha):
    return ha * 10000

def c_a_f(c):
    return (c * 9/5) + 32

def km_a_ha(km):
    return (km * 1000 * 1000) / 10000