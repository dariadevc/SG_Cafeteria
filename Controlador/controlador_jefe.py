from Visual.vista_jefe import VistaJefe
from Controlador.controlador_jefe_usuario import ControladorJefeUsuario

import Controlador.controlador_inicio
from Controlador.controlador_venta import ControladorVenta
from Controlador.controlador_stock import ControladorStock


class ControladorJefe:

    def __init__(self, usuario, id_usuario):
        self.__vista_jefe = VistaJefe(self)
        self.__vista_jefe.show()
        self._usuario = usuario
        self.__id_usuario = id_usuario
        nombre_usuario = self._usuario.get_usuario()

        self.__controlador_venta = ControladorVenta(usuario, self.__id_usuario)
        self.__vista_venta = self.__controlador_venta.get_vista()

        self.__controlador_stock = ControladorStock()
        self.__vista_stock = self.__controlador_stock.get_vista()

        self.__controlador_usuario = ControladorJefeUsuario()
        self.__vista_usuario = self.__controlador_usuario.get_vista()

        # self.__controlador_informe = ControladorInforme()
        # self.__vista_informe = self.__controlador_informe.get_vista()

        self.__vista_jefe.agregar_seccion(self.__vista_venta)
        self.__vista_jefe.agregar_seccion(self.__vista_stock)
        # self.__vista_jefe.agregar_seccion(self.__vista_informe)
        self.__vista_jefe.agregar_seccion(self.__vista_usuario)

        self.__vista_jefe.boton_venta.clicked.connect(self.cambio_a_venta)
        self.__vista_jefe.boton_stock.clicked.connect(self.cambio_a_stock)
        self.__vista_jefe.boton_informe.clicked.connect(self.cambio_a_informe)
        self.__vista_jefe.boton_usuario.clicked.connect(self.cambio_a_usuario)

        self.__vista_jefe.boton_cerrar.clicked.connect(self.cerrar_sesion)
        self.cambio_a_venta()
        self.__vista_jefe.show()

    def cerrar_sesion(self):
        self.__cerrar = Controlador.controlador_inicio.ControladorInicioSesion()
        self.__vista_jefe.close()

    def cambio_a_venta(self):
        self.__vista_jefe.cambiar_vista(0)
        self.__vista_jefe.actualizar_color_boton(self.__vista_jefe.boton_venta)
        # print("venta click")

    def cambio_a_stock(self):
        self.__vista_jefe.cambiar_vista(1)
        self.__vista_jefe.actualizar_color_boton(self.__vista_jefe.boton_stock)
        # print("stock click")

    def cambio_a_informe(self):
        self.__vista_jefe.cambiar_vista(3)
        self.__vista_jefe.actualizar_color_boton(self.__vista_jefe.boton_stock)
        # print("informe click")

    def cambio_a_usuario(self):
        self.__vista_jefe.cambiar_vista(2)
        self.__vista_jefe.actualizar_color_boton(self.__vista_jefe.boton_usuario)
        # print("usuario click")
