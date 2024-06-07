from Visual_dos.ventana_eliminar_producto import VentanaEliminarProducto
from Modelo_dos.producto_DAO import ProductoDAO


class ControladorEliminarProducto:

    def __init__(self, codigo_producto):
        self.__ventana_eliminar = VentanaEliminarProducto(self)
        self.__ventana_eliminar.show()
        self.__codigo_producto = codigo_producto

    def eliminar_producto(self):
        producto_dao = ProductoDAO()
        causa = self.__ventana_eliminar.combo_box.currentText()
        producto_dao.eliminar_producto(self.__codigo_producto, causa)
