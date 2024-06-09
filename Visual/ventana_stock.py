from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class VentanaStock(QWidget):

    def __init__(self, controlador):
        super().__init__()
        self.layout_ppal = QHBoxLayout()

        ###################################################
        self.tabla_productos = QTableWidget()
        self.tabla_productos.setColumnCount(7)
        self.tabla_productos.setFixedSize(550, 450)
        self.tabla_productos.setColumnWidth(0, 20)
        self.tabla_productos.setColumnWidth(1, 100)  ##descripcion
        self.tabla_productos.setColumnWidth(2, 80)  ##categoria
        self.tabla_productos.setColumnWidth(3, 80)  ##fecha
        self.tabla_productos.setColumnWidth(4, 70)  ##cantidad
        self.tabla_productos.setColumnWidth(5, 60)  ##stockminimo
        # self.tabla_productos.setColumnWidth(6,50)##vigencia
        # self.tabla_productos.setColumnWidth(7,95)

        # self.tabla_productos.setHorizontalHeaderLabels(["cod","Descripcion","Cat","FechaMod","Cantidad","StockMin","Precio","Baja","Causa"])
        self.tabla_productos.setHorizontalHeaderLabels(
            [
                "Cod",
                "Descripcion",
                "Categoría",
                "FechaMod",
                "Cantidad",
                "StockMin",
                "Precio",
            ]
        )
        self.tabla_productos.verticalHeader().setVisible(False)
        self.tabla_productos.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.tabla_productos.setStyleSheet("background-color: white;")
        self.tabla_productos.horizontalHeader().setStyleSheet(
            "background-color: lightblue; font-weight: bold;"
        )
        self.tabla_productos.cellClicked.connect(self.selecciono_fila)
        ###################################################
        self.layout_botonera = QVBoxLayout()

        icon = QPixmap(
             "C://Users//camus//Desktop//SG_Cafeteria//codigomodificado//Visual_dos//imagenes//refrescar3.jpg"
        ).scaled(25, 25)

        self.boton_refrescar_tabla = QPushButton()
        self.boton_refrescar_tabla.setStyleSheet("background-color: lightblue;")
        self.boton_refrescar_tabla.setFixedSize(80, 30)
        self.boton_refrescar_tabla.setIcon(QIcon(icon))
        self.boton_refrescar_tabla.setIconSize(icon.size())
        self.boton_agregar_producto = QPushButton("AGREGAR PRODUCTO")
        self.boton_agregar_producto.setStyleSheet("background-color: lightblue;")
        self.boton_agregar_producto.setFixedSize(120, 70)
        self.boton_modificar_producto = QPushButton("MODIFICAR PRODUCTO")
        self.boton_modificar_producto.setStyleSheet("background-color: lightblue;")
        self.boton_modificar_producto.setFixedSize(120, 70)
        self.boton_eliminar_producto = QPushButton("ELIMINAR PRODUCTO")
        self.boton_eliminar_producto.setStyleSheet("background-color: lightblue;")
        self.boton_eliminar_producto.setFixedSize(120, 70)

        self.boton_agregar_producto.clicked.connect(controlador.agregar_producto)
        self.boton_modificar_producto.clicked.connect(controlador.modificar_producto)
        self.boton_eliminar_producto.clicked.connect(controlador.eliminar_producto)
        self.boton_refrescar_tabla.clicked.connect(controlador.cargar_productos)

        self.layout_botonera.addWidget(self.boton_refrescar_tabla)
        self.layout_botonera.addWidget(self.boton_agregar_producto)
        self.layout_botonera.addWidget(self.boton_modificar_producto)
        self.layout_botonera.addWidget(self.boton_eliminar_producto)
        self.layout_botonera.setContentsMargins(10, 0, 0, 10)

        self.layout_ppal.addWidget(self.tabla_productos)
        self.layout_ppal.addLayout(self.layout_botonera)

        self.setLayout(self.layout_ppal)

    def selecciono_fila(self):
        self.tabla_productos.selectRow(self.tabla_productos.currentRow())

    def limpiar_tabla(self):
        self.tabla_productos.clearContents()

    def actualizar_color_boton(self, boton_seleccionado):
        botones = [
            self.boton_refrescar_tabla,
            self.boton_agregar_producto,
            self.boton_modificar_producto,
            self.boton_eliminar_producto,
        ]
        for boton in botones:
            if boton == boton_seleccionado:
                boton.setStyleSheet("background-color: lightgray;")
            else:
                boton.setStyleSheet("background-color: lightblue;")