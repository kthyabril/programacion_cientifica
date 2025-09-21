import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

class Generador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Contraseñas")
        self.layout = QVBoxLayout()
        self.boton = QPushButton("Generar")
        self.resultado = QLabel("")

        self.layout.addWidget(self.boton)
        self.layout.addWidget(self.resultado)
        self.setLayout(self.layout)

        self.boton.clicked.connect(self.mostrar)

    def mostrar(self):
        self.resultado.setText(generar_contraseña())

app = QApplication([])
ventana = Generador()
ventana.show()
app.exec_()