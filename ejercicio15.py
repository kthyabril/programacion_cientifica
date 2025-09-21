from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPalette, QColor

app = QApplication([])
ventana = QWidget()
ventana.setWindowTitle("Ejemplo PyQt")
ventana.resize(400, 300)  

boton = QPushButton("Presioname", ventana)
boton.setGeometry(100, 100, 200, 50)
boton.setStyleSheet("background-color: lightblue; color: black; font-size: 16px")  # ✅ Color personalizado

ventana.show()
app.exec_()