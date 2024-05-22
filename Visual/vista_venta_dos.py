from vista_cabecera import VistaCabecera
from vista_ticket import VistaTicket
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

class VentanaVenta (VistaCabecera):
    
    def __init__(self):
        super().__init__()
        self.boton_venta.setStyleSheet("background-color: rgb(135, 206, 235);")
        
        layout_venta = QHBoxLayout()
        self.layout_botones_venta = QVBoxLayout()
        
        boton_generar_ticket = QPushButton("GENERAR TICKET")
        boton_generar_ticket.setFixedSize(100,80)
        boton_generar_ticket.setStyleSheet("background-color: lightblue;")
        boton_anular_venta = QPushButton("ANULAR VENTA")
        boton_anular_venta.setFixedSize(100,80)
        boton_anular_venta.setStyleSheet("background-color: lightblue;")
        self.layout_botones_venta.addWidget(boton_generar_ticket)
        self.layout_botones_venta.addWidget(boton_anular_venta)
        self.layout_botones_venta.setContentsMargins(0,50,10,50)
        
        lbl_bienvenida = QLabel("BIENVENIDO A LA SECCION DE VENTAS")
        lbl_bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        self.stacked_botones.addWidget(lbl_bienvenida)
        self.stacked_botones.addWidget(VistaTicket())
        self.stacked_botones.setCurrentIndex(0)
        
        self.contenedor = QGroupBox()
        self.contenedor.setStyleSheet("background-color: lightblue;")
        self.contenedor.setLayout(self.stacked_botones)
        self.contenedor.setFixedSize(550,440)
        
        layout_venta.addLayout(self.layout_botones_venta)
        layout_venta.addWidget(self.contenedor)
        self.layout_principal.addLayout(layout_venta)
        
        widget = QWidget()
        widget.setLayout(self.layout_principal)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = VentanaVenta()
window.show()
app.exec()