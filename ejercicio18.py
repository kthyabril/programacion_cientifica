from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSpinBox, QPushButton
from PyQt5.QtCore import QTimer

class Temporizador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temporizador de Horno")
        self.resize(300, 200)

        self.layout = QVBoxLayout()
        self.spin = QSpinBox()
        self.spin.setRange(1, 120)
        self.label = QLabel("Tiempo restante:")
        self.boton = QPushButton("Iniciar")

        self.layout.addWidget(self.spin)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.boton)
        self.setLayout(self.layout)

        self.boton.clicked.connect(self.iniciar)
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar)

    def iniciar(self):
        self.tiempo = self.spin.value() * 60
        self.timer.start(1000)

    def actualizar(self):
        self.tiempo -= 1
        minutos = self.tiempo // 60
        segundos = self.tiempo % 60
        self.label.setText(f"{minutos:02d}:{segundos:02d}")
        if self.tiempo <= 0:
            self.timer.stop()
            self.label.setText("¡Tiempo cumplido!")
            self.setStyleSheet("background-color: red")  # ✅ Estrategia de aviso

app = QApplication([])
ventana = Temporizador()
ventana.show()
app.exec_()