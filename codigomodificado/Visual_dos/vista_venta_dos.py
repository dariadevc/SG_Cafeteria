from Visual_dos.vista_cabecera import VistaCabecera
from Visual_dos.vista_ticket import VistaTicket
from Visual_dos.vista_anular import VistaAnular
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class VentanaVenta (VistaCabecera):
    
    def __init__(self, controlador):
        super().__init__()
        self.boton_venta.setStyleSheet("background-color: rgb(135, 206, 235);")
        layout_venta = QHBoxLayout()
        self.layout_botones_venta = QVBoxLayout()
        self.boton_generar_ticket = QPushButton("GENERAR\n TICKET")
        self.boton_generar_ticket.setFixedSize(70,80)
        self.boton_generar_ticket.setStyleSheet("background-color: lightblue;")
        self.boton_anular_venta = QPushButton("ANULAR\n VENTA")
        self.boton_anular_venta.setFixedSize(70,80)
        self.boton_anular_venta.setStyleSheet("background-color: lightblue;")
        self.layout_botones_venta.addWidget(self.boton_generar_ticket)
        self.layout_botones_venta.addWidget(self.boton_anular_venta)
        self.layout_botones_venta.setContentsMargins(0,50,10,50)

        lbl_bienvenida = QLabel("BIENVENIDO A LA SECCION DE VENTAS")
        lbl_bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        #self.vista_ticket = VistaTicket()
#        self.vista_anular = VistaAnular()

        #self.stacked_botones.addWidget(lbl_bienvenida)
        #self.stacked_botones.addWidget(self.vista_ticket)
        #self.stacked_botones.addWidget(self.vista_anular)
        
        self.contenedor = QGroupBox()
        self.contenedor.setStyleSheet("background-color: lightblue;")
        #self.contenedor.setLayout(self.stacked_botones)
        self.contenedor.setFixedSize(600,500)
        
        layout_venta.addLayout(self.layout_botones_venta)
        layout_venta.addWidget(self.contenedor)
        self.layout_principal.addLayout(layout_venta)
        
        self.boton_cerrar.clicked.connect(controlador.cerrar_sesion)
        self.boton_stock.clicked.connect(controlador.cambio_a_stock)
        self.boton_informe.clicked.connect(controlador.cambio_a_informe)
        self.boton_generar_ticket.clicked.connect(controlador.cambio_a_generar)
        self.boton_anular_venta.clicked.connect(controlador.cambio_a_anular)
        
        self.setLayout(self.layout_principal)

    # def obtener_vista_ticket(self):
    #     return self.vista_ticket