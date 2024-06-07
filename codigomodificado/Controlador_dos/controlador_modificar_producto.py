import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Visual_dos.ventana_modificar_producto import VentanaModificarProducto
from Modelo_dos.producto_DAO import ProductoDAO


class ControladorModificarUsuario:

    def __init__(self, datos_producto):
        self.__ventana_modificar = VentanaModificarProducto(self)
        self.__ventana_modificar.label_1.setText(
            f"{self.__ventana_modificar.label_1.text()} {datos_producto[1]}"
        )
        self.__ventana_modificar.show()
        self.cargar_producto_a_modificar(datos_producto)

    def cargar_producto_a_modificar(self, datos_producto):
        self.__ventana_modificar.label_dni.setText(f"{datos_producto[1]}")
        self.__ventana_modificar.input_1.setText(datos_producto[2])
        self.__ventana_modificar.input_2.setText(datos_producto[3])
        self.__ventana_modificar.input_3.setText(datos_producto[5])
        self.__ventana_modificar.input_4.setText(datos_producto[6])

    def modificar_usuario(self):
        dni_usuario = self.__ventana_modificar.label_dni.text()
        nombre_modificado = self.__ventana_modificar.input_1.text()
        apellido_modificado = self.__ventana_modificar.input_2.text()
        nombre_usuario_modificado = self.__ventana_modificar.input_3.text()
        contrasenia_modificada = self.__ventana_modificar.input_4.text()
        ProductoDAO().modificar_usuario(
            dni_usuario,
            nombre_modificado,
            apellido_modificado,
            nombre_usuario_modificado,
            contrasenia_modificada,
        )
