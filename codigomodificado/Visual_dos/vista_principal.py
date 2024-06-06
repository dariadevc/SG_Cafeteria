from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class VistaPrincipal(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.setWindowTitle("Cafeteria Viera")
        self.boton_cerrar = QPushButton("Cerrar\nSesion")
        self.boton_cerrar.setFixedSize(80, 60)
        self.boton_cerrar.setStyleSheet("background-color: lightblue;")

        self.label = QLabel("Nombre y Apellido")
        self.label.setFixedSize(500, 60)
        self.label.setContentsMargins(0, 20, 0, 0)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.imagen = QLabel("foto")
        # pixmap = QPixmap("C:/Users/Alambrito/Documents/GitHub/SG_Cafeteria/Visual/imagenes/foto_usuario.jpg")
        pixmap = QPixmap(
            "C:/Users/Daria/Desktop/Universidad/Cursada_2024/200/220/223_POO/POO_CC/SG_Cafeteria/codigomodificado/Visual_dos/imagenes/foto_usuario.jpg"
        )
        self.imagen.setPixmap(pixmap.scaled(100, 80))
        self.imagen.setFixedSize(100, 80)
        self.imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setFixedSize(750, 640)
        self.layout_principal = QVBoxLayout()

        layout_usuario = QHBoxLayout()
        self.layout_botones = QHBoxLayout()

        self.boton_venta = QPushButton("VENTA")
        self.boton_venta.setStyleSheet("background-color: lightblue;")
        self.boton_stock = QPushButton("STOCK")
        self.boton_stock.setStyleSheet("background-color: lightblue;")
        self.boton_informe = QPushButton("INFORME")
        self.boton_informe.setStyleSheet("background-color: lightblue;")

        layout_usuario.setContentsMargins(20, 0, 0, 0)
        layout_usuario.addWidget(self.boton_cerrar)
        layout_usuario.addWidget(self.label)
        layout_usuario.addWidget(self.imagen)

        self.layout_botones.addWidget(self.boton_venta)
        self.layout_botones.addWidget(self.boton_stock)
        self.layout_botones.addWidget(self.boton_informe)

        self.stacked_layout = QStackedLayout()

        self.layout_principal.addLayout(layout_usuario)
        self.layout_principal.addLayout(self.layout_botones)
        self.layout_principal.addLayout(self.stacked_layout)

        self.setLayout(self.layout_principal)

    def cambiar_vista(self, index):
        self.stacked_layout.setCurrentIndex(index)

    def agregar_seccion(self, vista):
        self.stacked_layout.addWidget(vista)

    def actualizar_color_boton(self, boton_seleccionado):
        botones = [self.boton_venta, self.boton_stock, self.boton_informe]
        for boton in botones:
            if boton == boton_seleccionado:
                boton.setStyleSheet("background-color: lightgray;")
            else:
                boton.setStyleSheet("background-color: lightblue;")
