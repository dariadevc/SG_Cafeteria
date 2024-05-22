from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class VistaCabecera (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.label = QLabel("Nombre y Apellido")
        self.label.setFixedSize(600,80)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.imagen = QLabel("foto")
        self.imagen.setFixedSize(100,80)
        self.imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setFixedSize(700,600)
        self.layout_principal = QVBoxLayout()
        
        layout_usuario = QHBoxLayout()
        self.layout_botones = QHBoxLayout()
        
        self.boton_venta = QPushButton("VENTA")
        self.boton_venta.setFixedSize(216,25)
        self.boton_venta.setStyleSheet("background-color: lightblue;")
        self.boton_stock = QPushButton("STOCK")
        self.boton_stock.setFixedSize(216,25)
        self.boton_stock.setStyleSheet("background-color: lightblue;")
        self.boton_informe = QPushButton("INFORME")
        self.boton_informe.setStyleSheet("background-color: lightblue;")
        self.boton_informe.setFixedSize(216,25)
        
        layout_usuario.addWidget(self.label)
        layout_usuario.addWidget(self.imagen)
        
        self.layout_botones.addWidget(self.boton_venta)
        self.layout_botones.addWidget(self.boton_stock)
        self.layout_botones.addWidget(self.boton_informe)
        
        self.stacked_botones = QStackedLayout()
        
        self.layout_principal.addLayout(layout_usuario)
        self.layout_principal.addLayout(self.layout_botones)