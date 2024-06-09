from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class VentanaEliminarUsuario (QWidget):
    
    def __init__(self, controlador):
        super().__init__()
        
        self.setFixedSize(QSize(400,300))
        
        palette = QPalette()
        palette.setColor(QPalette.ColorGroup.All, QPalette.ColorRole.Window, QColor(135, 206, 235)) #color de la ventana
        self.setPalette(palette)
        
        self.layout_ventana = QVBoxLayout()
        self.layout_ventana.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_ventana.setSpacing(30)
        self.label_1 = QLabel("Bienvenido a Eliminar Usuario")
        self.label_1.setStyleSheet("font: bold;")
        self.label_2 = QLabel("Cuál es la causa de la eliminación del usuario ")
        self.label_2.setStyleSheet("font: bold;")
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Bajo Rendimiento","Comportamiento Indebido","Faltas Injustificadas","Sucesivas Inpuntualidades"])
        
        self.boton_eliminar = QPushButton("Eliminar Usuario")
        self.boton_eliminar.clicked.connect(controlador.eliminar_usuario)
        
        self.layout_ventana.addWidget(self.label_1)
        self.layout_ventana.addWidget(self.label_2)
        self.layout_ventana.addWidget(self.combo_box)
        self.layout_ventana.addWidget(self.boton_eliminar)
        
        self.setLayout(self.layout_ventana)