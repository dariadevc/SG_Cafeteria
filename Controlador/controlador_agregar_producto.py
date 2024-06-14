from Visual.ventana_agregar_producto import VentanaAgregarProducto
from Modelo.producto import Producto


class ControladorAgregarProducto:

    def __init__(self):
        self.__ventana_agregar_producto = VentanaAgregarProducto(self)
        self.__ventana_agregar_producto.show()

    def agregar_producto_a_bd(self):
        try:
            descripcion = self.__ventana_agregar_producto.line_edit_1.text()
            categoria = self.categoria_a_letra(
                self.__ventana_agregar_producto.combo_box_categoria.currentText()
            )
            cantidad = int(self.__ventana_agregar_producto.line_edit_3.text())
            stock_minimo = int(self.__ventana_agregar_producto.line_edit_4.text())
            precio = self.__ventana_agregar_producto.line_edit_5.text()
            datos = [descripcion,categoria,cantidad,stock_minimo,precio]
            if None in datos or '' in datos:
                raise ValueError
            else:
                datos_validados = ["",descripcion,categoria,None,cantidad,stock_minimo,precio,"","",]
                producto_nuevo = Producto(datos_validados)
                producto_nuevo.agregar_a_bd()
                self.__ventana_agregar_producto.notifico_insercion(descripcion)
                self.__ventana_agregar_producto.hide()
        except:
            self.__ventana_agregar_producto.imprimo_alerta()

    def categoria_a_letra(self, categoria):
        if categoria == "Bebida":
            return "A"
        elif categoria == "Comida":
            return "B"
        elif categoria == "Helados":
            return "C"
