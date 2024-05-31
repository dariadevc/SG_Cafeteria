from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class VentanaModificarUsuario (QWidget):
    
    def __init__(self, controlador):
        super().__init__()
        
        self.setFixedSize(QSize(400,300))
        
        palette = QPalette()
        palette.setColor(QPalette.ColorGroup.All, QPalette.ColorRole.Window, QColor(135, 206, 235)) #color de la ventana
        self.setPalette(palette)
        
        layout_modificar_usuario = QVBoxLayout()
        layout_modificar_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label_0 = QLabel("Bienvenido a Modificar Usuario")
        self.label_0.setStyleSheet("font: bold;")
        self.label_1 = QLabel("DNI del Usuario a Modificar: ")
        self.label_1.setStyleSheet("font: bold;")
        self.label_dni = QLabel()
        self.label_2 = QLabel("Ingrese el nuevo Nombre")
        self.label_2.setStyleSheet("font: bold;")
        self.input_1 = QLineEdit()
        self.input_1.setPlaceholderText("nombre")
        
        self.label_3 = QLabel("Ingrese el nuevo Apellido")
        self.label_3.setStyleSheet("font: bold;")
        self.input_2 = QLineEdit()
        self.input_2.setPlaceholderText("apellido")
        
        self.label_4 = QLabel("Ingrese el nuevo nombre_usuario")
        self.label_4.setStyleSheet("font: bold;")
        self.input_3 = QLineEdit()
        self.input_3.setPlaceholderText("nombre_usuario")
        
        self.label_5 = QLabel("Ingrese la nueva contraseña")
        self.label_5.setStyleSheet("font: bold;")
        self.input_4 = QLineEdit()
        self.input_4.setPlaceholderText("contraseña")
        
        self.boton_modificar = QPushButton("Guardar Usuario")
        self.boton_modificar.clicked.connect(controlador.modificar_usuario)
        
        layout_modificar_usuario.addWidget(self.label_0)
        layout_modificar_usuario.addWidget(self.label_1)
        layout_modificar_usuario.addWidget(self.label_2)
        layout_modificar_usuario.addWidget(self.input_1)
        layout_modificar_usuario.addWidget(self.label_3)
        layout_modificar_usuario.addWidget(self.input_2)
        layout_modificar_usuario.addWidget(self.label_4)
        layout_modificar_usuario.addWidget(self.input_3)
        layout_modificar_usuario.addWidget(self.label_5)
        layout_modificar_usuario.addWidget(self.input_4)
        layout_modificar_usuario.addWidget(self.boton_modificar)
        
        self.setLayout(layout_modificar_usuario)