from __future__ import annotations
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QPushButton,
    QLabel,
    QSizePolicy,
)
from PyQt6.QtCore import Qt


class VentanaPedido(QWidget):
    closed = pyqtSignal()

    def __init__(self, controlador, nro_mesa):
        super().__init__()
        self.setWindowTitle("Pedido Mesa " + str(nro_mesa))
        self.setFixedSize(750, 500)
        self.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.controlador = controlador
        self.botones_sumar = []
        self.botones_restar = []
        self.etiquetas_cantidad = []
        self.productos_agregados = []
        self.pedidos_realizados = []
        self.stock = []

        # self.imagenes_x_subido = QPixmap(
        #     "C://SG_Cafeteria//Visual//imagenes//check.jpg"
        # ).scaled(10, 10)
        # self.imagenes_menos_subido = QPixmap(
        #     "C://SG_Cafeteria//Visual//imagenes//-.jfif"
        # ).scaled(10, 10)
        # self.imagenes_mas_subido = QPixmap(
        #     "C://SG_Cafeteria//Visual//imagenes//+.jfif"
        # ).scaled(10, 10)
        self.imagenes_x_subido = QPixmap(
            "C://Users//camus//Desktop//SG_Cafeteria//codigomodificado//Visual_dos//imagenes//check.jpg"
        ).scaled(10, 10)
        self.imagenes_menos_subido = QPixmap(
            "C://Users//camus//Desktop//SG_Cafeteria//codigomodificado//Visual_dos//imagenes//-.jfif"
        ).scaled(10, 10)
        self.imagenes_mas_subido = QPixmap(
            "C://Users//camus//Desktop//SG_Cafeteria//codigomodificado//Visual_dos//imagenes//+.jfif"
        ).scaled(10, 10)

        self.contenedor = QVBoxLayout()
        self.contenedor.setSpacing(30)

        self.contenedor_nombres = QHBoxLayout()
        self.etiqueta_comida = QLabel("Bebidas")
        self.etiqueta_comida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiqueta_comida.setStyleSheet(
            "background-color: darkblue; color: white; font-size: 14px; font-weight: bold;"
        )
        self.etiqueta_bebida = QLabel("Comida")
        self.etiqueta_bebida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiqueta_bebida.setStyleSheet(
            "background-color: darkblue; color: white; font-size: 14px; font-weight: bold;"
        )
        self.etiqueta_helado = QLabel("Helados")
        self.etiqueta_helado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiqueta_helado.setStyleSheet(
            "background-color: darkblue; color: white; font-size: 14px; font-weight: bold;"
        )

        self.contenedor_nombres.addWidget(self.etiqueta_comida)
        self.contenedor_nombres.addWidget(self.etiqueta_bebida)
        self.contenedor_nombres.addWidget(self.etiqueta_helado)

        self.contenedor.addLayout(self.contenedor_nombres)

        self.tabla_alta = QHBoxLayout()
        self.tabla_alta.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        self.tabla_comida = QVBoxLayout()
        self.tabla_bebidas = QVBoxLayout()
        self.tabla_helados = QVBoxLayout()

        self.tabla_alta.addLayout(self.tabla_comida)
        self.tabla_alta.addLayout(self.tabla_bebidas)
        self.tabla_alta.addLayout(self.tabla_helados)

        self.contenedor.addLayout(self.tabla_alta)

        self.tabla_baja = QHBoxLayout()
        self.tabla_total = QHBoxLayout()
        self.tabla_baja.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.scroll_layout.setSpacing(1)
        self.tabla_pedido = QVBoxLayout()
        spacio_pedido = QSpacerItem(
            1000, 600, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )
        self.tabla_pedido.addSpacerItem(spacio_pedido)

        self.tabla_pedido.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignRight
        )
        self.scroll_layout.addLayout(self.tabla_pedido)
        ## Botón finalizar pedido
        self.boton_finalizar_pedido = QPushButton("IMPRIMIR TICKET")
        font = QFont()
        font.setBold(True)
        self.boton_finalizar_pedido.setFont(font)
        self.tamano_botones = QSize(130, 60)
        self.boton_finalizar_pedido.setFixedSize(self.tamano_botones)
        self.boton_finalizar_pedido.setStyleSheet(
            "background-color: lightblue; font-size: 14px; font-weight: bold;"
        )
        self.boton_finalizar_pedido.clicked.connect(controlador.finalizar_pedido)

        ## Botón anular pedido
        self.boton_anular_pedido = QPushButton("ANULAR PEDIDO")
        font = QFont()
        font.setBold(True)
        self.boton_anular_pedido.setFont(font)
        self.boton_anular_pedido.setFixedSize(self.tamano_botones)
        self.boton_anular_pedido.setStyleSheet(
            "background-color: lightblue; font-size: 14px; font-weight: bold;"
        )
        self.boton_anular_pedido.clicked.connect(controlador.anular_pedido)

        # Layout botones
        self.botones_pedido = QVBoxLayout()
        self.botones_pedido.addWidget(self.boton_finalizar_pedido)
        self.botones_pedido.addWidget(self.boton_anular_pedido)

        self.etiqueta_total = QLabel("TOTAL  :  $  ")
        self.etiqueta_total.setFixedWidth(200)
        self.etiqueta_total.setStyleSheet(
            "background-color: white; font-size: 14px; font-weight: bold;"
        )
        self.etiqueta_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabla_total.addWidget(self.etiqueta_total)

        self.tabla_baja.addWidget(self.scroll_area)

        self.tabla_baja.addLayout(self.botones_pedido)

        self.contenedor.addLayout(self.tabla_alta)
        self.contenedor.addLayout(self.tabla_baja)
        self.contenedor.addLayout(self.tabla_total)

        self.setLayout(self.contenedor)

    def agregarFilaConBotones(self, layout, descripcion_producto):
        fila_layout = QHBoxLayout()
        tamano_etiqueta = QSize(300, 15)
        tamano_botones = QSize(15, 15)

        etiqueta_producto = QLabel(descripcion_producto)
        etiqueta_producto.setStyleSheet("font-size: 14px;")
        etiqueta_producto.setFixedSize(tamano_etiqueta)
        etiqueta_producto.setFixedWidth(600)

        boton_menos = QPushButton()
        boton_menos.setFixedSize(tamano_botones)
        boton_menos.setIcon(QIcon(self.imagenes_menos_subido))
        boton_menos.setIconSize(self.imagenes_menos_subido.size())
        boton_menos.setStyleSheet(
            "background-color: none; padding-top: 7px; padding-bottom: 5px;"
        )
        boton_menos.setProperty("accion", "restar")
        boton_menos.clicked.connect(self.controlador.boton_presionado)

        boton_cantidad = QLabel("0")
        boton_cantidad.setFixedSize(tamano_botones)

        boton_mas = QPushButton()
        boton_mas.setFixedSize(tamano_botones)
        boton_mas.setIcon(QIcon(self.imagenes_mas_subido))
        boton_mas.setIconSize(self.imagenes_mas_subido.size())
        boton_mas.setStyleSheet(
            "background-color: none; padding-top: 7px; padding-bottom: 5px;"
        )
        boton_mas.setProperty("accion", "sumar")
        boton_mas.clicked.connect(self.controlador.boton_presionado)

        fila_layout.addWidget(etiqueta_producto)
        fila_layout.addWidget(boton_menos)
        fila_layout.addWidget(boton_cantidad)
        fila_layout.addWidget(boton_mas)
        layout.addLayout(fila_layout)
        self.botones_sumar.append(boton_mas)
        self.botones_restar.append(boton_menos)
        self.etiquetas_cantidad.append(boton_cantidad)
        self.productos_agregados.append((etiqueta_producto.text(), 0))

    def agregarFilaConBotonEliminar(self, layout, descripcion, precio):

        fila_layout = QHBoxLayout()
        fila_layout.setSpacing(20)
        fila_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        tamano_etiqueta = QSize(250, 15)
        tamano_botones = QSize(15, 15)

        boton_eliminar = QPushButton()
        boton_eliminar.setFixedSize(tamano_botones)
        boton_eliminar.setIcon(QIcon(self.imagenes_x_subido))
        boton_eliminar.setIconSize(self.imagenes_x_subido.size())
        boton_eliminar.setStyleSheet(
            "background-color: none; padding-top: 7px; padding-bottom: 5px;"
        )

        etiqueta_descripcion = QLabel(descripcion)
        etiqueta_descripcion.setStyleSheet("font-size: 14px;")
        etiqueta_descripcion.setFixedSize(tamano_etiqueta)
        etiqueta_descripcion.setFixedWidth(120)

        etiqueta_relleno = QLabel(" X ")
        etiqueta_relleno.setStyleSheet("font-size: 14px;")
        etiqueta_relleno.setFixedSize(tamano_etiqueta)
        etiqueta_relleno.setFixedWidth(40)

        etiqueta_cantidad = QLabel("")
        etiqueta_cantidad.setStyleSheet("font-size: 14px;")
        etiqueta_cantidad.setFixedSize(tamano_etiqueta)
        etiqueta_cantidad.setFixedWidth(40)

        etiqueta_precio = QLabel("$")
        etiqueta_precio.setStyleSheet("font-size: 14px;")
        etiqueta_precio.setFixedSize(tamano_etiqueta)
        etiqueta_precio.setFixedWidth(40)

        precio = QLabel(f"{precio:.2f}")
        etiqueta_precio.setStyleSheet("font-size: 14px;")
        precio.setFixedSize(tamano_etiqueta)
        precio.setFixedWidth(50)

        fila_layout.addWidget(boton_eliminar)
        fila_layout.addWidget(etiqueta_descripcion)
        fila_layout.addWidget(etiqueta_relleno)
        fila_layout.addWidget(etiqueta_cantidad)
        fila_layout.addWidget(etiqueta_precio)
        fila_layout.addWidget(precio)

        layout.insertLayout(0, fila_layout)
        return fila_layout

    # Para saber si se cerró una ventana
    def closeEvent(self, event):
        self.controlador.cerrar_ventana_pedido()
        event.accept()
