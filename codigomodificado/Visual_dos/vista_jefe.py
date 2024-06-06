from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Visual_dos.vista_principal import VistaPrincipal
from PyQt6.QtGui import *


class VistaJefe(VistaPrincipal):

    def __init__(self, controlador):
        super().__init__()

        # self.bienvenida = QLabel("Bienvenidooo")
        # self.bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.boton_usuario = QPushButton("USUARIO")
        self.boton_usuario.setStyleSheet("background-color:lightblue")
        self.layout_botones.addWidget(self.boton_usuario)

        self.stacked_layout.addWidget(self.bienvenida)
        self.stacked_layout.setCurrentIndex(0)

        self.boton_usuario.clicked.connect(controlador.cambio_a_usuario)
        self.boton_informe.clicked.connect(controlador.cambio_a_informe)
        self.boton_venta.clicked.connect(controlador.cambio_a_venta)
        self.boton_stock.clicked.connect(controlador.cambio_a_stock)
        self.boton_cerrar.clicked.connect(controlador.cerrar_sesion)
