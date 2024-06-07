from Visual_dos.ventana_agregar_producto import VentanaAgregarProducto
from Modelo_dos.producto_DAO import ProductoDAO

class ControladorAgregarProducto:
    
    def __init__(self):
        self.__ventana_agregar_producto = VentanaAgregarProducto(self)
        self.__ventana_agregar_producto.show()
        self.__producto_dao = ProductoDAO()
    
    def agregar_producto_a_bd (self):
        descripcion = self.__ventana_agregar_producto.line_edit_1.text()
        cantidad = int(self.__ventana_agregar_producto.line_edit_2.text())
        stock_minimo = int(self.__ventana_agregar_producto.line_edit_3.text())
        precio = self.__ventana_agregar_producto.line_edit_4.text()
        self.__producto_dao = ProductoDAO()
        self.__producto_dao.agregar_producto(descripcion,cantidad,stock_minimo,precio)