from PyQt5.QtWidgets import QApplication, QMainWindow
from ventana_convertida import Ui_MainWindow

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.saludar)

    def saludar(self):
        print("Hola soy Katherine")

app = QApplication([])
ventana = MiVentana()
ventana.show()
app.exec_()