from Visual.vista_cabecera import VistaCabecera
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
#from Visual.layout_venta import VistaVenta
class VistaVendedor (VistaCabecera):
    
    def __init__(self):
        super().__init__()
        
        layout_vendedor = QVBoxLayout()
        lbl_bienvenida_vendedor = QLabel("BIENVENIDO USUARIO VENDEDOR")
        lbl_bienvenida_vendedor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_vendedor.addWidget(lbl_bienvenida_vendedor)
        
        #self.stacked_botones.addWidget(lbl_bienvenida_vendedor)
        #self.stacked_botones.addWidget(VistaVenta())
        self.layout_principal.addLayout(layout_vendedor)
        
        widget = QWidget()
        widget.setLayout(self.layout_principal)
        self.setCentralWidget(widget)