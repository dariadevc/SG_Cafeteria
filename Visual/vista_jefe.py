from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Visual.vista_venta import VistaVenta
import sys

class VistaJefe (QMainWindow):
    
    def __init__(self, controlador):
        super().__init__()
        layout_principal = QVBoxLayout()


        ##                  NOMBRE
        nombre_sg = QLabel("SISTEMA DE GESTION DE CAFETERIA")
        nombre_sg.setFixedSize(600,50)
        nombre_sg.setStyleSheet("background-color: lightblue")
        layout_principal.addWidget(nombre_sg)


        ##             LOGO DE SISTEMA DE GESTION Y NOMBRE DEL INGRESANTE
        layout_segunda_presentacion = QHBoxLayout()
        logo_cafeteria = QLabel("Aca deberia ir el logo de la cafeteria")
        logo_cafeteria.setFixedSize(450,50)
        logo_cafeteria.setStyleSheet("background-color: #f6b009")
        datos = QLabel("Nombre del Usuario")
        datos.setStyleSheet("background-color: #f6b009")
        datos.setFixedSize(150,50)
        layout_segunda_presentacion.addWidget(logo_cafeteria)
        layout_segunda_presentacion.addWidget(datos)


        ##                       BOTONES
        layout_barra_navegacion = QHBoxLayout()
        self.btn_venta = QPushButton("Gestion de Ventas")
        btn_stock = QPushButton("Gestion de Stock")
        btn_informe = QPushButton("Informes")
        self.btn_venta.setStyleSheet("background-color: #816561")
        btn_stock.setStyleSheet("background-color: cyan")
        btn_informe.setStyleSheet("background-color: #637d96")
        layout_barra_navegacion.addWidget(self.btn_venta)
        layout_barra_navegacion.addWidget(btn_stock)
        layout_barra_navegacion.addWidget(btn_informe)

        layout_principal.addLayout(layout_segunda_presentacion)
        layout_principal.addLayout(layout_barra_navegacion)
        
        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(VistaVenta())
        layout_principal.addLayout(self.stack_layout)

        widget = QWidget()
        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)