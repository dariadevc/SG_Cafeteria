from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

class BotoneraVenta(QMainWindow):
    
    def __init__(self):
        super().__init__()
        layout_principal = QHBoxLayout()
        lbl_bienvenida = QLabel("BIENVENIDO A LA SECCION DE VENTAS")
        #lbl_bienvenida.setFixedSize(600,300)
        lbl_bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ##########################################################
        layout_botones = QVBoxLayout()
        
        boton_generar_ticket = QPushButton("GENERAR TICKET")
        boton_generar_ticket.setFixedSize(100,80)
        boton_generar_ticket.setStyleSheet("background-color: lightblue;")
        boton_anular_venta = QPushButton("ANULAR VENTA")
        boton_anular_venta.setFixedSize(100,80)
        boton_anular_venta.setStyleSheet("background-color: lightblue;")
        layout_botones.addWidget(boton_generar_ticket)
        layout_botones.addWidget(boton_anular_venta)
        layout_botones.setContentsMargins(0,50,10,50)
        #########################################################
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(lbl_bienvenida)
        
        self.contenedor = QGroupBox()
        self.contenedor.setStyleSheet("background-color: lightblue;")
        self.contenedor.setLayout(self.stacked_layout)
        self.contenedor.setFixedSize(550,440)
        
        layout_principal.addLayout(layout_botones)
        layout_principal.addWidget(self.contenedor)
        
        widget = QWidget()
        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)
