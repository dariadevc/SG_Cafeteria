from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class VentanaAgregarProducto(QWidget):

    def __init__(self, controlador):
        super().__init__()
        self.setFixedSize(QSize(400, 500))

        palette = QPalette()
        palette.setColor(
            QPalette.ColorGroup.All, QPalette.ColorRole.Window, QColor(135, 206, 235)
        )  # color de la ventana
        self.setPalette(palette)

        self.frame = QFrame()
        layout_ventana_agregar = QVBoxLayout(self.frame)
        layout_ventana_agregar.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignHCenter
        )

        self.label_0 = QLabel("Bienvenido a Agregar Producto")
        self.label_0.setStyleSheet("color: black; font-size: 20px")
        layout_ventana_agregar.addWidget(self.label_0)

        #################################################################################

        self.label_1 = QLabel("Ingrese el nombre del Producto")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.label_1.setStyleSheet("color: black; font-size: 16px")
        self.line_edit_1 = QLineEdit()
        self.line_edit_1.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.line_edit_1.setPlaceholderText("nombre del producto")
        self.line_edit_1.setFixedSize(QSize(200, 30))
        self.line_edit_1.setStyleSheet("margin-right: 50px")

        self.label_2 = QLabel("Seleccione la categoría del producto")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setStyleSheet("color: black; font-size: 16px")
        self.combo_box_categoria = QComboBox()
        self.combo_box_categoria.addItems(["Comida", "Bebida", "Helados"])
        self.combo_box_categoria.setFixedSize(QSize(200, 30))

        self.label_3 = QLabel("Ingrese la cantidad actual")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setStyleSheet("color: black; font-size: 16px")
        self.line_edit_3 = QLineEdit()
        self.line_edit_3.setPlaceholderText("cantidad actual")
        self.line_edit_3.setFixedSize(QSize(200, 30))

        self.label_4 = QLabel("Ingrese el stock minimo")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setStyleSheet("color: black; font-size: 16px")
        self.line_edit_4 = QLineEdit()
        self.line_edit_4.setPlaceholderText("stock minimo")
        self.line_edit_4.setFixedSize(QSize(200, 30))

        self.label_5 = QLabel("Ingrese el precio del producto")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setStyleSheet("color: black; font-size: 16px")
        self.line_edit_5 = QLineEdit()
        self.line_edit_5.setPlaceholderText("precio del producto")
        self.line_edit_5.setFixedSize(QSize(200, 30))

        layout_ventana_agregar.addWidget(self.label_1)
        layout_ventana_agregar.addWidget(self.line_edit_1)
        layout_ventana_agregar.addWidget(self.label_2)
        layout_ventana_agregar.addWidget(self.combo_box_categoria)
        layout_ventana_agregar.addWidget(self.label_3)
        layout_ventana_agregar.addWidget(self.line_edit_3)
        layout_ventana_agregar.addWidget(self.label_4)
        layout_ventana_agregar.addWidget(self.line_edit_4)
        layout_ventana_agregar.addWidget(self.label_5)
        layout_ventana_agregar.addWidget(self.line_edit_5)
        self.boton_agregar_producto = QPushButton("Agregar Producto")
        self.boton_agregar_producto.setFixedSize(200, 30)
        layout_ventana_agregar.addWidget(self.boton_agregar_producto)

        self.boton_agregar_producto.clicked.connect(controlador.agregar_producto_a_bd)

        self.setLayout(layout_ventana_agregar)
