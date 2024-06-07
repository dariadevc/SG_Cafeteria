import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Visual_dos.ventana_stock import VentanaStock
from Modelo_dos.producto_DAO import ProductoDAO

# from Controlador_dos.controlador_modificar_producto import ControladorModificarProducto
from Controlador_dos.controlador_agregar_producto import ControladorAgregarProducto
from Controlador_dos.controlador_eliminar_producto import ControladorEliminarProducto
from PyQt6.QtWidgets import *


class ControladorStock:

    def __init__(self, usuario):
        self.__ventana_stock = VentanaStock(self)
        self.__producto_dao = ProductoDAO()
        self.__ventana_stock.show()
        self.cargar_productos()

    def cargar_productos(self):
        self.__ventana_stock.limpiar_tabla()
        productos = self.__producto_dao.obtener_todos_productos()
        self.__ventana_stock.tabla_productos.setRowCount(len(productos))
        for fila, producto in enumerate(productos):
            descripcion = QTableWidgetItem(f"{producto[1]}")
            categoria = QTableWidgetItem(f"{producto[2]}")
            fecha_mod = QTableWidgetItem(f"{producto[3]}")
            cantidad = QTableWidgetItem(f"{producto[4]}")
            stock_min = QTableWidgetItem(f"{producto[5]}")
            precio_unitario = QTableWidgetItem(f"{producto[6]}")
            vigente = QTableWidgetItem(f"{producto[7]}")
            causa = QTableWidgetItem(f"{producto[8]}")

            self.__ventana_stock.tabla_productos.setItem(fila, 0, descripcion)
            self.__ventana_stock.tabla_productos.setItem(fila, 1, categoria)
            self.__ventana_stock.tabla_productos.setItem(fila, 2, fecha_mod)
            self.__ventana_stock.tabla_productos.setItem(fila, 3, cantidad)
            self.__ventana_stock.tabla_productos.setItem(fila, 4, stock_min)
            self.__ventana_stock.tabla_productos.setItem(fila, 5, precio_unitario)
            self.__ventana_stock.tabla_productos.setItem(fila, 6, vigente)
            self.__ventana_stock.tabla_productos.setItem(fila, 7, causa)

    def get_vista(self):
        return self.__ventana_stock

    def agregar_producto(self):
        self.__controlador_agregar_producto = ControladorAgregarProducto()

    # def modificar_producto (self):
    #     self.__controlador_modificar_producto = ControladorModificarProducto()

    def eliminar_producto(self):
        self.__controlador_eliminar_producto = ControladorEliminarProducto()
