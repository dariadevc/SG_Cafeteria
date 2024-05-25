from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class VistaCabecera (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(135, 206, 235);")
        
        self.btn_cerrar = QPushButton("Cerrar\nSesion")
        self.btn_cerrar.setFixedSize(80,60)
        self.btn_cerrar.setStyleSheet("background-color: lightblue;")
        
        self.label = QLabel("Nombre y Apellido")
        self.label.setFixedSize(500,60)
        self.label.setContentsMargins(0,20,0,0)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.imagen = QLabel("foto")
        pixmap = QPixmap("C:/Users/Alambrito/Documents/GitHub/SG_Cafeteria/Visual/imagenes/foto_usuario.jpg")
        self.imagen.setPixmap(pixmap.scaled(100,80))
        self.imagen.setFixedSize(100,80)
        self.imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setFixedSize(750,670)
        self.layout_principal = QVBoxLayout()
        
        layout_usuario = QHBoxLayout()
        self.layout_botones = QHBoxLayout()
        
        self.boton_venta = QPushButton("VENTA")
        self.boton_venta.setFixedSize(220,25)
        self.boton_venta.setStyleSheet("background-color: lightblue;")
        self.boton_stock = QPushButton("STOCK")
        self.boton_stock.setFixedSize(220,25)
        self.boton_stock.setStyleSheet("background-color: lightblue;")
        self.boton_informe = QPushButton("INFORME")
        self.boton_informe.setStyleSheet("background-color: lightblue;")
        self.boton_informe.setFixedSize(220,25)
        
        layout_usuario.setContentsMargins(20,0,0,0)
        layout_usuario.addWidget(self.btn_cerrar)
        layout_usuario.addWidget(self.label)
        layout_usuario.addWidget(self.imagen)
        
        self.layout_botones.addWidget(self.boton_venta)
        self.layout_botones.addWidget(self.boton_stock)
        self.layout_botones.addWidget(self.boton_informe)
        
        self.stacked_botones = QStackedLayout()
        
        self.layout_principal.addLayout(layout_usuario)
        self.layout_principal.addLayout(self.layout_botones)