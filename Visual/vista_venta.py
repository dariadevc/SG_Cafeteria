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
            boton_mesa.setStyleSheet(
                "background-color: lightgreen; font-weight: bold; font-size: 16px;"
            )
            fila = (i - 1) // num_columnas
            columna = (i - 1) % num_columnas
            grid_layout.addWidget(boton_mesa, fila, columna)
            self.botones_mesas.append(boton_mesa)
            boton_mesa.clicked.connect(
                lambda checked, mesa=i: controlador.seleccionar_mesa(mesa)
            )

        # Crear un layout para los indicadores de color
        self.indicadores_color = QHBoxLayout()

        # Crear los cuadrados de color y las etiquetas correspondientes
        self.crear_indicador_color("lightgreen", "Disponible")
        self.crear_indicador_color("rgb(255, 109, 109)", "Ocupada")

        # Crear un widget contenedor para los indicadores de color
        self.widget_indicadores = QWidget()
        self.widget_indicadores.setLayout(self.indicadores_color)

        # Crear un contenedor para los botones de las mesas y los indicadores
        self.contenedor = QGroupBox()
        self.contenedor.setStyleSheet("background-color: lightblue;")
        self.contenedor.setFixedSize(600, 500)

        # Crear un layout vertical para el contenedor principal
        layout_contenedor = QVBoxLayout()

        # Añadir un espaciador vertical antes del grid layout para centrarlo
        layout_contenedor.addSpacerItem(
            QSpacerItem(
                20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )
        )

        # Añadir el grid layout que contiene los botones de las mesas
        layout_contenedor.addLayout(grid_layout)

        # Añadir otro espaciador después del grid layout para centrarlo
        layout_contenedor.addSpacerItem(
            QSpacerItem(
                20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )
        )

        # Añadir un espaciador fijo de 30px
        layout_contenedor.addSpacing(30)

        # Añadir el widget contenedor de indicadores de color al layout del contenedor principal
        layout_contenedor.addWidget(
            self.widget_indicadores,
            alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom,
        )

        self.contenedor.setLayout(layout_contenedor)

        # Añadir el contenedor al layout principal
        layout_principal = QHBoxLayout()
        layout_principal.addWidget(self.contenedor)
        self.setLayout(layout_principal)

    def crear_indicador_color(self, color, texto):
        # Crear el layout para un indicador de color
        indicador_layout = QHBoxLayout()

        # Crear el cuadrado de color
        cuadro_color = QLabel()
        cuadro_color.setFixedSize(15, 15)
        cuadro_color.setStyleSheet(
            f"background-color: {color};border: 1px solid black;"
        )

        # Crear la etiqueta de texto
        etiqueta = QLabel(texto)
        etiqueta.setStyleSheet("font-size: 14px;")

        # Añadir el cuadrado de color y la etiqueta al layout del indicador
        indicador_layout.addWidget(cuadro_color)
        indicador_layout.addWidget(etiqueta)

        # Añadir el layout del indicador al layout de indicadores de color
        self.indicadores_color.addLayout(indicador_layout)

    def actualizar_estado_mesas(self, mesas_ocupadas):
        for i, boton in enumerate(self.botones_mesas):
            if (i + 1) in mesas_ocupadas:
                boton.setStyleSheet(
                    "background-color: rgb(255, 109, 109); font-weight: bold; font-size: 16px;"
                )
            else:
                boton.setStyleSheet(
                    "background-color: lightgreen; font-weight: bold; font-size: 16px;"
                )
