from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class VentanaModificarProducto(QWidget):

    def __init__(self, controlador):
        super().__init__()

        self.setFixedSize(QSize(400, 350))

        palette = QPalette()
        palette.setColor(
            QPalette.ColorGroup.All, QPalette.ColorRole.Window, QColor(135, 206, 235)
        )  # color de la ventana
        self.setPalette(palette)

        layout_modificar = QVBoxLayout()
        layout_modificar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_bienvenida = QVBoxLayout()

        self.label_0 = QLabel("Bienvenido a Modificar Producto")
        self.label_0.setStyleSheet("font: bold;")

        layout_bienvenida.addWidget(self.label_0)

        self.label_1 = QLabel("Codigo del Producto a Modificar: ")
        self.label_1.setStyleSheet("font: bold;")
        self.label_cod = QLabel()
        self.label_2 = QLabel("Ingrese el nuevo Nombre")
        self.label_2.setStyleSheet("font: bold;")
        self.input_1 = QLineEdit()
        self.input_1.setPlaceholderText("nombre del producto")

        self.label_3 = QLabel("Seleccione la categoría del producto")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setStyleSheet("color: black; font-size: 16px")
        self.combo_box_categoria = QComboBox()
        self.combo_box_categoria.addItems(["Comida", "Bebida", "Helados"])
        self.combo_box_categoria.setFixedSize(QSize(200, 30))

        self.label_4 = QLabel("Ingrese la nueva cantidad")
        self.label_4.setStyleSheet("font: bold;")
        self.input_2 = QLineEdit()
        self.input_2.setPlaceholderText("cantidad del producto")

        self.label_5 = QLabel("Ingrese el nuevo stock minimo")
        self.label_5.setStyleSheet("font: bold;")
        self.input_3 = QLineEdit()
        self.input_3.setPlaceholderText("stock minimo")

        self.label_5 = QLabel("Ingrese el nuevo Precio del producto")
        self.label_5.setStyleSheet("font: bold;")
        self.input_4 = QLineEdit()
        self.input_4.setPlaceholderText("precio")

        self.boton_modificar = QPushButton("Guardar Cambios")
        self.boton_modificar.clicked.connect(controlador.modificar_producto)

        layout_bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_bienvenida.setSpacing(20)
        layout_modificar.addLayout(layout_bienvenida)
        layout_modificar.addWidget(self.label_1)
        layout_modificar.addWidget(self.label_2)
        layout_modificar.addWidget(self.input_1)
        layout_modificar.addWidget(self.label_3)
        layout_modificar.addWidget(self.combo_box_categoria)
        layout_modificar.addWidget(self.input_2)
        layout_modificar.addWidget(self.label_4)
        layout_modificar.addWidget(self.input_3)
        layout_modificar.addWidget(self.label_5)
        layout_modificar.addWidget(self.input_4)
        layout_modificar.addWidget(self.boton_modificar)

        self.setLayout(layout_modificar)
