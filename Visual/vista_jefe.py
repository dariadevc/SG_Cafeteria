from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Visual.vista_venta import VistaVenta
from Visual.vista_stock import VistaStock
import sys
from PyQt6.QtGui import *

class VistaJefe (QMainWindow):
    
    def __init__(self, controlador):
        super().__init__()
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('#437a37'))
        layout_principal = QVBoxLayout()
        self.setWindowTitle("SG - Cafeteria")
        self.setPalette(palette)


        ##                  NOMBRE
        nombre_sg = QLabel("SISTEMA DE GESTION DE CAFETERIA")
        nombre_sg.setFixedSize(600,50)
        nombre_sg.setStyleSheet("background-color: lightblue")
        nombre_sg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(nombre_sg)


        ##             LOGO DE SISTEMA DE GESTION Y NOMBRE DEL INGRESANTE
        layout_segunda_presentacion = QHBoxLayout()
        self.logo_cafeteria = QLabel("Aca deberia ir el logo de la cafeteria")
        self.logo_cafeteria.setFixedSize(450,50)
        self.logo_cafeteria.setStyleSheet("background-color: #f6b009")
        self.nombre = QLabel("Hola  ")
        self.nombre.setStyleSheet("background-color: #f6b009")
        self.nombre.setFixedSize(150,50)
        layout_segunda_presentacion.addWidget(self.logo_cafeteria)
        layout_segunda_presentacion.addWidget(self.nombre)


        ##                       BOTONES
        layout_barra_navegacion = QHBoxLayout()
        self.btn_venta = QPushButton("Gestion de Ventas")
        self.btn_stock = QPushButton("Gestion de Stock")
        self.btn_usuario = QPushButton("Gestion de Usuarios")
        self.btn_informe = QPushButton("Informes")

        self.btn_venta.setStyleSheet("background-color: #637d96")
        self.btn_stock.setStyleSheet("background-color: #637d96")
        self.btn_usuario.setStyleSheet("background-color: #637d96")
        self.btn_informe.setStyleSheet("background-color: #637d96")

        layout_barra_navegacion.addWidget(self.btn_venta)
        layout_barra_navegacion.addWidget(self.btn_stock)
        layout_barra_navegacion.addWidget(self.btn_usuario)
        layout_barra_navegacion.addWidget(self.btn_informe)

        layout_principal.addLayout(layout_segunda_presentacion)
        layout_principal.addLayout(layout_barra_navegacion)
        
        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(VistaVenta())
        self.stack_layout.addWidget(VistaStock())
        layout_principal.addLayout(self.stack_layout)

        widget = QWidget()
        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)