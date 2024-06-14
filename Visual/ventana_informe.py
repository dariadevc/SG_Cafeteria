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

        self.contenedor.addLayout(self.referencias_layout)

    def crear_referencia(self, color, texto):
        referencia_layout = QHBoxLayout()

        cuadro_color = QLabel()
        cuadro_color.setFixedSize(15, 15)
        cuadro_color.setStyleSheet(
            f"background-color: {color}; border: 1px solid black;"
        )

        etiqueta = QLabel(texto)
        etiqueta.setStyleSheet("font-size: 14px;")

        referencia_layout.addWidget(cuadro_color)
        referencia_layout.addWidget(etiqueta)

        self.referencias_layout.addLayout(referencia_layout)
