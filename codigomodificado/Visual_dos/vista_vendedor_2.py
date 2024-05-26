from Visual_dos.vista_cabecera import VistaCabecera
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class VistaVendedor (VistaCabecera):
    
    def __init__(self, controlador):
        super().__init__()
        
        layout_vendedor = QVBoxLayout()
        lbl_bienvenida_vendedor = QLabel("BIENVENIDO USUARIO VENDEDOR")
        lbl_bienvenida_vendedor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_vendedor.addWidget(lbl_bienvenida_vendedor)
        
        #self.stacked_botones.addWidget(lbl_bienvenida_vendedor)
        #self.stacked_botones.addWidget(VistaVenta())
        self.layout_principal.addLayout(layout_vendedor)
        
        
        self.boton_cerrar.clicked.connect(controlador.logout)
        self.boton_venta.clicked.connect(controlador.cambio_a_venta)
        self.boton_stock.clicked.connect(controlador.cambio_a_stock)
        self.boton_informe.clicked.connect(controlador.cambio_a_informe)
        
        self.setLayout(self.layout_principal)