from __future__ import annotations
import sys

# sys.path.append('C://Users//camus//Desktop//SG_Cafeteria//Modelo')
from Modelo.producto_DAO import ProductoDAO


class Producto:
    def __init__(self, datos):
        self.__cod_producto = datos[0]
        self.__descripcion = datos[1]
        self.__categoria = datos[2]
        self.__fecha_modif = datos[3]
        self.__stock_actual = datos[4]
        self.__stock_min = datos[5]
        self.__precio_unitario = datos[6]
        self.__vigente = datos[7]
        self.__causa = datos[8]
        self.__productodao = ProductoDAO()

    ## Getters y Setters

    def get_cod(self):
        print("Se solicitó el código del producto.")
        return self.__cod_producto

    def get_descripcion(self):
        print("Se solicitó la descripcion del producto.")
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
        print("Se modificó la descripcion del producto.")

    def get_categoria(self):
        print("Se solicitó la categoria del producto.")
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria
        print("Se modificó la categoria del producto.")

    def get_fecha_modif(self):
        print("Se solicitó el fecha_modif del producto.")
        return self.__fecha_modif

    def set_fecha_modif(self, fecha_modif):
        self.__fecha_modif = fecha_modif
        print("Se modificó el fecha_modif del producto.")

    def get_causa(self):
        print("Se solicitó el causa del producto.")
        return self.__causa

    def set_causa(self, causa):
        self.__causa = causa
        print("Se modificó el causa del producto.")

    def get_stock_actual(self):
        print("Se solicitó el stock actual del producto.")
        return self.__stock_actual

    def set_stock_actual(self, stock_actual):
        self.__stock_actual = stock_actual
        print("Se modificó el stock actual del producto.")

    def get_stock_min(self):
        print("Se solicitó el stock_min del producto.")
        return self.__stock_min

    def set_stock_min(self, stock_min):
        self.__stock_min = stock_min
        print("Se modificó el stock_min del producto.")

    def get_precio_unitario(self):
        print("Se solicitó el precio_unitario del producto.")
        return self.__precio_unitario

    def set_precio_unitario(self, precio_unitario):
        self.__precio_unitario = precio_unitario
        print("Se modificó el precio_unitario del producto.")

    def get_vigente(self):
        print("Se solicitó el vigente del producto.")
        return self.__vigente

    def set_vigente(self, vigente):
        self.__vigente = vigente
        print("Se modificó el vigente del producto.")

    def datos_producto(self):
        return f"DESCRIPCIÓN: {self.__descripcion} | CATEGORIA: {self.__categoria} | FECHA MODIFICACIÓN: {self.__fecha_modif} | STOCK ACTUAL: {self.__stock_actual} | STOCK MÍNIMO: {self.__stock_min}  | VIGENCIA: {self.__vigente}"

    def agregar_a_bd(self):
        self.__productodao.agregar_producto(
            self.__descripcion,
            self.__categoria,
            self.__stock_actual,
            self.__stock_min,
            self.__precio_unitario,
        )
