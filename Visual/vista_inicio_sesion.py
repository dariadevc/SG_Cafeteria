from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

class VistaInicioSesion(QMainWindow):
    
    def __init__(self, controlador):
        super().__init__()
        self.setWindowTitle("SISTEMA DE GESTION DE CAFETERIA")
        self.setFixedSize(400,500)

        layout = QVBoxLayout()

        lbl_nombre = QLabel("Ingrese su nombre de usuario")
        lbl_nombre.setFixedSize(250,50)
        lbl_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.campo_nombre = QLineEdit()
        self.campo_nombre.setFixedSize(250,20)

        lbl_contraseña = QLabel("Ingrese su contraseña")
        lbl_contraseña.setFixedSize(250,50)
        lbl_contraseña.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.campo_contraseña = QLineEdit()
        self.campo_contraseña.setEchoMode(QLineEdit.EchoMode(2))
        self.campo_contraseña.setFixedSize(250,20)

        combo_1 = QComboBox()
        combo_1.addItems(["Vendedor","Jefe"])

        btn = QPushButton("Registrarse")
        btn.setFixedSize(110,30)
        btn.clicked.connect(controlador.valido_entrada)

        layout_2 = QHBoxLayout()
        layout_2.addWidget(btn)

        layout.addWidget(lbl_nombre)
        layout.addWidget(self.campo_nombre)
        layout.addWidget(lbl_contraseña)
        layout.addWidget(self.campo_contraseña)
        layout.addWidget(combo_1)
        layout.addLayout(layout_2)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()