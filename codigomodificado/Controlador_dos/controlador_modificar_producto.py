from Visual_dos.ventana_modificar_producto import VentanaModificarProducto
from Modelo_dos.producto_DAO import ProductoDAO


class ControladorModificarProducto:

    def __init__(self, datos_producto):
        self.__ventana_modificar = VentanaModificarProducto(self)
        self.__ventana_modificar.label_1.setText(
            f"{self.__ventana_modificar.label_1.text()} {datos_producto[1]}"
        )
        self.__ventana_modificar.show()
        self.cargar_producto_a_modificar(datos_producto)

    def cargar_producto_a_modificar(self, datos_producto):
        self.__ventana_modificar.label_cod.setText(f"{datos_producto[0]}")
        self.__ventana_modificar.input_1.setText(datos_producto[1])
        self.__ventana_modificar.input_2.setText(str(datos_producto[4]))
        self.__ventana_modificar.input_3.setText(str(datos_producto[5]))
        self.__ventana_modificar.input_4.setText(str(datos_producto[6]))

    def modificar_producto(self):
        codigo = self.__ventana_modificar.label_cod.text()
        descripcion_modificada = self.__ventana_modificar.input_1.text()
        cantidad_modificada = int(self.__ventana_modificar.input_2.text())
        stockminimo_modificado = int(self.__ventana_modificar.input_3.text())
        precio_modificado = self.__ventana_modificar.input_4.text()
        ProductoDAO().modificar_producto(codigo,descripcion_modificada,cantidad_modificada,stockminimo_modificado,precio_modificado)
