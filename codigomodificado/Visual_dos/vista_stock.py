from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class VistaStock(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #1f3e53")
        self.setFixedSize(600, 400)
        self.setMaximumSize(600, 400)
        self.setMinimumSize(600, 400)

        layout_principal = QHBoxLayout()

        ######################################################
        tabla_productos = QTableWidget()
        tabla_productos.setColumnCount(5)
        tabla_productos.setRowCount(10)
        tabla_productos.setFixedSize(400, 380)
        layout_principal.addWidget(tabla_productos)

        ######################################################
        layout_derecho = QVBoxLayout()
        btn_agregar_producto = QPushButton("Agregar Producto")
        btn_agregar_producto.setFixedSize(100, 50)
        btn_agregar_producto.setStyleSheet("background-color: #36536a")
        btn_eliminar_producto = QPushButton("Eliminar Producto")
        btn_eliminar_producto.setFixedSize(100, 50)
        btn_eliminar_producto.setStyleSheet("background-color: #36536a")

        layout_derecho.addWidget(btn_agregar_producto)
        layout_derecho.addWidget(btn_eliminar_producto)
        ######################################################

        layout_principal.addLayout(layout_derecho)
        # widget = QWidget()
        self.setLayout(layout_principal)
        # self.setCentralWidget(widget)
