from Visual.vista_principal import VistaPrincipal
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class VistaVendedor(VistaPrincipal):

    def __init__(self, controlador):
        super().__init__()

        # self.lbl_bienvenida_vendedor = QLabel("BIENVENIDO USUARIO VENDEDOR")
        # self.lbl_bienvenida_vendedor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # self.stacked_layout.addWidget(self.lbl_bienvenida_vendedor)
        # self.cambiar_vista(0)

        self.boton_cerrar.clicked.connect(controlador.logout)
        self.boton_venta.clicked.connect(controlador.cambio_a_venta)
        self.boton_stock.clicked.connect(controlador.cambio_a_stock)
        self.boton_informe.clicked.connect(controlador.cambio_a_informe)
