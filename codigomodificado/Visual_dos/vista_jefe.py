from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
#from Visual_dos.vista_venta import VistaVenta
#from Visual_dos.vista_stock import VistaStock
from Visual_dos.vista_principal import VistaPrincipal
from PyQt6.QtGui import *

class VistaJefe (VistaPrincipal):
    
    def __init__(self, controlador):
        super().__init__()
        
        self.bienvenida = QLabel("Bienvenidooo")
        self.bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.boton_usuario = QPushButton("USUARIO")
        
        self.layout_botones.addWidget(self.boton_usuario)
        
        self.stacked_layout.addWidget(self.bienvenida)
        self.stacked_layout.setCurrentIndex(0)
        
        self.boton_venta.clicked.connect(controlador.cambio_a_venta)
        self.boton_stock.clicked.connect(controlador.cambio_a_stock)
        self.boton_cerrar.clicked.connect(controlador.cerrar_sesion)
        
        #self.setLayout(self.layout_principal)