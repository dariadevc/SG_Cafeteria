from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Visual.vista_principal import VistaPrincipal
from PyQt6.QtGui import *


class VistaJefe(VistaPrincipal):

    def __init__(self, nombre_apellido, controlador):
        super().__init__(nombre_apellido)

        self.boton_usuario = QPushButton("USUARIO")
        self.boton_usuario.setStyleSheet(
            "background-color:lightblue; font-size: 14px; font-weight: bold;"
        )
        self.layout_botones.addWidget(self.boton_usuario)
        self._lista_botones.append(self.boton_usuario)
        self.boton_usuario.clicked.connect(controlador.cambio_a_usuario)
        self.boton_informe.clicked.connect(controlador.cambio_a_informe)
        self.boton_venta.clicked.connect(controlador.cambio_a_venta)
        self.boton_stock.clicked.connect(controlador.cambio_a_stock)
        self.boton_cerrar.clicked.connect(controlador.cerrar_sesion)
