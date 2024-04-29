from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("vistaDelUsuario")
        self.setFixedSize(400,500)

        layout = QVBoxLayout()

        lbl_nombre = QLabel("Ingrese su nombre de usuario")
        lbl_nombre.setFixedSize(250,50)
        lbl_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.qle_nombre = QLineEdit()
        self.qle_nombre.setFixedSize(250,20)

        lbl_contraseña = QLabel("Ingrese su contraseña")
        lbl_contraseña.setFixedSize(250,50)
        lbl_contraseña.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.qle_contraseña = QLineEdit()
        self.qle_contraseña.setEchoMode(QLineEdit.EchoMode(2))
        self.qle_contraseña.setFixedSize(250,20)

        btn = QPushButton("Registrarse")
        btn.setFixedSize(110,30)

        layout.addWidget(lbl_nombre)
        layout.addWidget(self.qle_nombre)
        layout.addWidget(lbl_contraseña)
        layout.addWidget(self.qle_contraseña)
        layout.addWidget(btn)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()