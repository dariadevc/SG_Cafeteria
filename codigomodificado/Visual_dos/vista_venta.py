from Visual_dos.vista_principal import VistaPrincipal
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class VentanaVenta(QWidget):

    def __init__(self, controlador):
        super().__init__()
        self.setStyleSheet("background-color: rgb(135, 206, 235);")
        layout_venta = QHBoxLayout()

        # Crear un layout de rejilla para organizar los botones en una matriz
        grid_layout = QGridLayout()

        # Crear 10 botones, cada uno representando una mesa, y añadirlos al grid_layout
        self.botones_mesas = []
        num_filas = 2
        num_columnas = 5
        for i in range(1, 11):
            boton_mesa = QPushButton(f"Mesa {i}")
            boton_mesa.setFixedSize(100, 100)
            boton_mesa.setStyleSheet("background-color: lightgreen;")
            fila = (i - 1) // num_columnas
            columna = (i - 1) % num_columnas
            grid_layout.addWidget(boton_mesa, fila, columna)
            self.botones_mesas.append(boton_mesa)
            boton_mesa.clicked.connect(
                lambda checked, mesa=i: controlador.seleccionar_mesa(mesa)
            )

        # Crear un contenedor para los botones de las mesas
        self.contenedor = QGroupBox()
        self.contenedor.setStyleSheet("background-color: lightblue;")
        self.contenedor.setFixedSize(600, 500)
        self.contenedor.setLayout(grid_layout)

        # Añadir el contenedor al layout principal
        layout_principal = QHBoxLayout()
        layout_principal.addWidget(self.contenedor)
        self.setLayout(layout_principal)

        # self.boton_cerrar.clicked.connect(controlador.cerrar_sesion)
        # self.boton_stock.clicked.connect(controlador.cambio_a_stock)
        # self.boton_informe.clicked.connect(controlador.cambio_a_informe)
        # self.boton_generar_ticket.clicked.connect(controlador.cambio_a_generar)
        # self.boton_anular_venta.clicked.connect(controlador.cambio_a_anular)

    def actualizar_estado_mesas(self, mesas_ocupadas):
        for i, boton in enumerate(self.botones_mesas):
            if (i + 1) in mesas_ocupadas:
                boton.setStyleSheet("background-color: lightgrey;")
            else:
                boton.setStyleSheet("background-color: lightgreen;")


# antiguo venta
# self.layout_botones_venta = QVBoxLayout()
# self.boton_generar_ticket = QPushButton("GENERAR\n TICKET")
# self.boton_generar_ticket.setFixedSize(70,80)
# self.boton_generar_ticket.setStyleSheet("background-color: lightblue;")
# self.boton_anular_venta = QPushButton("ANULAR\n VENTA")
# self.boton_anular_venta.setFixedSize(70,80)
# self.boton_anular_venta.setStyleSheet("background-color: lightblue;")
# self.layout_botones_venta.addWidget(self.boton_generar_ticket)
# self.layout_botones_venta.addWidget(self.boton_anular_venta)
# self.layout_botones_venta.setContentsMargins(0,50,10,50)

# lbl_bienvenida = QLabel("BIENVENIDO A LA SECCION DE VENTAS")
# lbl_bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
# layout = QVBoxLayout()
# layout.addWidget(lbl_bienvenida)

# self.contenedor = QGroupBox()
# self.contenedor.setStyleSheet("background-color: lightblue;")
# self.contenedor.setFixedSize(600,500)
# self.contenedor.setLayout(layout)
# layout_venta.addLayout(self.layout_botones_venta)
# layout_venta.addWidget(self.contenedor)
# widget_venta = QWidget()
# widget_venta.setLayout(layout_venta)
# self.stacked_layout.addWidget(widget_venta)
# self.stacked_layout.setCurrentIndex(0)
