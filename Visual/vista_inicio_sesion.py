from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

class VistaInicioSesion(QMainWindow):
    
    def __init__(self, controlador):
        super().__init__()
        self.setWindowTitle("SISTEMA DE GESTION DE CAFETERIA")
        self.setFixedSize(400,500)
        self.setStyleSheet("background-color: #29621f")

        layout = QVBoxLayout()

        lbl_nombre = QLabel("Ingrese su nombre de usuario")
        lbl_nombre.setFixedSize(250,50)
        lbl_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.campo_nombre = QLineEdit()
        self.campo_nombre.setFixedSize(250,20)
        self.campo_nombre.setStyleSheet("background-color: white")

        lbl_contraseña = QLabel("Ingrese su contraseña")
        lbl_contraseña.setFixedSize(250,50)
        lbl_contraseña.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.campo_contraseña = QLineEdit()
        self.campo_contraseña.setEchoMode(QLineEdit.EchoMode(2))
        self.campo_contraseña.setFixedSize(250,20)
        self.campo_contraseña.setStyleSheet("background-color: white")

        self.combo_1 = QComboBox()
        self.combo_1.addItems(["Vendedor","Jefe"])
        self.combo_1.setStyleSheet("background-color: white")

        btn = QPushButton("Registrarse")
        btn.setFixedSize(110,30)
        btn.clicked.connect(controlador.valido_entrada)

        layout_2 = QHBoxLayout()
        layout_2.addWidget(btn)

        self.estado = QLabel()
        self.estado.setText("Datos Incorrectos")
        self.estado.setStyleSheet("color: red")
        self.estado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.estado.hide()

        layout.addWidget(lbl_nombre)
        layout.addWidget(self.campo_nombre)
        layout.addWidget(lbl_contraseña)
        layout.addWidget(self.campo_contraseña)
        layout.addWidget(self.combo_1)
        layout.addLayout(layout_2)
        layout.addWidget(self.estado)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)