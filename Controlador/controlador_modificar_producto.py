from Visual.ventana_modificar_producto import VentanaModificarProducto
from Modelo.producto_DAO import ProductoDAO


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
        self.__ventana_modificar.combo_box_categoria.setCurrentText(
            self.categoria_a_cadena(datos_producto[2])
        )
        self.__ventana_modificar.input_2.setText(str(datos_producto[4]))
        self.__ventana_modificar.input_3.setText(str(datos_producto[5]))
        self.__ventana_modificar.input_4.setText(str(datos_producto[6]))

    def modificar_producto(self):
        codigo = self.__ventana_modificar.label_cod.text()
        descripcion_modificada = self.__ventana_modificar.input_1.text()
        categoria = self.categoria_a_letra(
            self.__ventana_modificar.combo_box_categoria.currentText()
        )
        cantidad_modificada = int(self.__ventana_modificar.input_2.text())
        stockminimo_modificado = int(self.__ventana_modificar.input_3.text())
        precio_modificado = self.__ventana_modificar.input_4.text()
        ProductoDAO().modificar_producto(
            codigo,
            categoria,
            descripcion_modificada,
            cantidad_modificada,
            stockminimo_modificado,
            precio_modificado,
        )

    def categoria_a_letra(self, categoria):
        if categoria == "Bebida":
            return "A"
        elif categoria == "Alimentos":
            return "B"
        elif categoria == "Helados":
            return "C"

    def categoria_a_cadena(self, categoria_codigo):
        if categoria_codigo == "A":
            return "Bebida"
        elif categoria_codigo == "B":
            return "Alimentos"
        elif categoria_codigo == "C":
            return "Helados"
        else:
            return "Desconocido"
