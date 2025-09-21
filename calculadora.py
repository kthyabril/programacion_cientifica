import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("300x400")  # Tamaño de ventana
root.title("Calculadora de Katherine")  # Nombre personalizado

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for fila in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn_text in fila:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", width=5, height=2,
                        bg="lightblue" if btn_text.isdigit() else "lightgray")
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()