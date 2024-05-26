from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Visual_dos.vista_venta import VistaVenta
from Visual_dos.vista_stock import VistaStock
from Visual_dos.vista_cabecera import VistaCabecera
from PyQt6.QtGui import *

class VistaJefe (VistaCabecera):
    
    def __init__(self, controlador):
        super().__init__()
        self.setWindowTitle("SG - Cafeteria")
        self.bienvenida = QLabel("Bienvenidooo")
        self.bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.boton_usuario = QPushButton("USUARIO")

        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(self.bienvenida)
        self.stack_layout.addWidget(VistaVenta())
        self.stack_layout.addWidget(VistaStock())
        
        self.layout_botones.addWidget(self.boton_usuario)
        self.layout_principal.addLayout(self.stack_layout)
        
        self.boton_venta.clicked.connect(controlador.cambio_a_venta)
        self.boton_stock.clicked.connect(controlador.cambio_a_stock)
        self.boton_cerrar.clicked.connect(controlador.cerrar_sesion)
        
        self.setLayout(self.layout_principal)