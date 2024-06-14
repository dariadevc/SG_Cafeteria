from __future__ import annotations
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class VentanaInforme(QWidget):
    def __init__(self, controlador):
        super().__init__()
        # self.setFixedSize(685, 550)
        self.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.controlador = controlador

        self.contenedor = QVBoxLayout(self)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.contenedor.addWidget(self.scroll_area)

        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)

        self.layout_graficos = QVBoxLayout(self.scroll_content)

        self.referencias_layout = QHBoxLayout()
        self.crear_referencia("firebrick", "Stock mínimo")
        self.crear_referencia("steelblue", "Cantidad actual")

        # Agregar las referencias al layout principal
        self.contenedor.addLayout(self.referencias_layout)

    def crear_referencia(self, color, texto):
        # Crear el layout para una referencia
        referencia_layout = QHBoxLayout()

        # Crear el cuadrado de color
        cuadro_color = QLabel()
        cuadro_color.setFixedSize(15, 15)
        cuadro_color.setStyleSheet(
            f"background-color: {color}; border: 1px solid black;"
        )

        # Crear la etiqueta de texto
        etiqueta = QLabel(texto)
        etiqueta.setStyleSheet("font-size: 14px;")

        # Añadir el cuadrado de color y la etiqueta al layout de la referencia
        referencia_layout.addWidget(cuadro_color)
        referencia_layout.addWidget(etiqueta)

        # Añadir el layout de la referencia al layout de referencias
        self.referencias_layout.addLayout(referencia_layout)


# class VentanaInforme(QWidget):
#     def __init__(self, controlador):
#         super().__init__()
#         # self.setWindowTitle("Informes")
#         self.setFixedSize(685, 550)
#         self.setStyleSheet("background-color: rgb(135, 206, 235);")
#         self.controlador = controlador

#         self.contenedor = QVBoxLayout(self)  # Layout principal horizontal
#         self.tabla_informe = QTableWidget()
#         self.tabla_informe.setColumnCount(1)
#         self.tabla_informe.verticalHeader().setVisible(False)
#         self.tabla_informe.horizontalHeader().setVisible(False)
#         self.referencias = QVBoxLayout()

#         self.contenedor.addWidget(self.tabla_informe)
#         self.contenedor.addLayout(self.referencias)
#         self.referencia = QLabel("Referencias : ")
#         self.referencia.setStyleSheet("font-size: 14px; font-weight: bold")
#         self.referencia_stock_minimo = QLabel("Stock minimo")
#         self.referencia_stock_minimo.setStyleSheet(
#             'color : "firebrick"; font-size: 14px; font-weight: bold'
#         )
#         self.referencia_cantidad_acutal = QLabel("Cantidad actual")
#         self.referencia_cantidad_acutal.setStyleSheet(
#             'color : "steelblue";font-size: 14px; font-weight: bold'
#         )
#         self.referencias.addWidget(self.referencia)
#         self.referencias.addWidget(self.referencia_stock_minimo)
#         self.referencias.addWidget(self.referencia_cantidad_acutal)
#         self.setLayout(self.contenedor)
