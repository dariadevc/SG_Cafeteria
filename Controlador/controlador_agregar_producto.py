from Visual.ventana_agregar_producto import VentanaAgregarProducto
from Modelo.producto import Producto


class ControladorAgregarProducto:

    def __init__(self):
        self.__ventana_agregar_producto = VentanaAgregarProducto(self)
        self.__ventana_agregar_producto.show()

    def agregar_producto_a_bd(self):
        descripcion = self.__ventana_agregar_producto.line_edit_1.text()
        categoria = self.categoria_a_letra(
            self.__ventana_agregar_producto.combo_box_categoria.currentText()
        )
        cantidad = int(self.__ventana_agregar_producto.line_edit_3.text())
        stock_minimo = int(self.__ventana_agregar_producto.line_edit_4.text())
        precio = self.__ventana_agregar_producto.line_edit_5.text()
        datos = [
            "",
            descripcion,
            categoria,
            None,
            cantidad,
            stock_minimo,
            precio,
            "",
            "",
        ]
        producto_nuevo = Producto(datos)
        producto_nuevo.agregar_a_bd()

    def categoria_a_letra(self, categoria):
        if categoria == "Comida":
            return "A"
        elif categoria == "Bebida":
            return "B"
        elif categoria == "Helados":
            return "C"
