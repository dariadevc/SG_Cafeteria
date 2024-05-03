import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from vista_stock import VistaStock

class VistaVendedora(QWidget):
    def __init__(self):
        super().__init__()
        


        self.setStyleSheet("background-color: #D2B48C;")
        layout_principal = QVBoxLayout(self)    
        cabecera_layout = QHBoxLayout()
        
      
        pixmap = QPixmap("C:/Users/camus/Desktop/PF Cafeteria POO/vista/logo.png")  
        label_imagen = QLabel()
        label_imagen.setPixmap(pixmap.scaled(200, 200))
        cabecera_layout.addWidget(label_imagen)
        
        label_cafeteria = QLabel(" USUARIO : ")
        label_cafeteria.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_cafeteria.setFixedSize(300, 30)
        label_cafeteria.setStyleSheet("color: white; background-color: #8B4513;")
        cabecera_layout.addWidget(label_cafeteria)
        
      
        label_usuario = QLabel("   ")
        label_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_usuario.setFixedSize(300, 30)
        label_usuario.setStyleSheet("color: white; background-color: #8B4513;") 
        cabecera_layout.addWidget(label_usuario)

       
        layout_principal.addLayout(cabecera_layout)
        

        comboboxes_layout = QHBoxLayout()
        for _ in range(4):
            combobox = QComboBox()
            combobox.setFixedWidth(120)
            comboboxes_layout.addWidget(combobox)

        layout_principal.addLayout(comboboxes_layout)
        
        
        vista_layout = QHBoxLayout()
        vista_venta = VistaStock()
        vista_layout.addWidget(vista_venta)
        
        
        layout_principal.addLayout(vista_layout)
        abajo_layout = QHBoxLayout()
        
      
        label_precio = QLabel(" PRECIO TOTAL  $ ")
        label_precio.setStyleSheet("color: white; background-color: #8B4513;")
        abajo_layout.addWidget(label_precio)
        
        
        precio_total = QLabel("  ")
        precio_total.setStyleSheet("color: white; background-color: #8B4513;")
        abajo_layout.addWidget(precio_total)
        
       
        boton = QPushButton(" IMPRIMIR TICKET ")
        boton.setStyleSheet("background-color: #8B4513; color: white;")
        abajo_layout.addWidget(boton)
        
       
        layout_principal.addLayout(abajo_layout)

