from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
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
        logo_cafeteria.setStyleSheet("background-color: lightblue")
        datos = QLabel("Nombre del Usuario")
        datos.setStyleSheet("background-color: lightblue")
        datos.setFixedSize(150,50)
        layout_segunda_presentacion.addWidget(logo_cafeteria)
        layout_segunda_presentacion.addWidget(datos)


        ##                       BOTONES
        layout_barra_navegacion = QHBoxLayout()
        btn_1 = QPushButton("Gestion de Ventas")
        btn_2 = QPushButton("Gestion de Stock")
        btn_3 = QPushButton("Informes")
        btn_1.setStyleSheet("background-color: yellow")
        btn_2.setStyleSheet("background-color: cyan")
        btn_3.setStyleSheet("background-color: blue")
        layout_barra_navegacion.addWidget(btn_1)
        layout_barra_navegacion.addWidget(btn_2)
        layout_barra_navegacion.addWidget(btn_3)

        layout_principal.addLayout(layout_segunda_presentacion)
        layout_principal.addLayout(layout_barra_navegacion)
        
        #stack_layout = QStackedLayout()
        #layout_principal.addLayout(stack_layout)

        widget = QWidget()
        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)