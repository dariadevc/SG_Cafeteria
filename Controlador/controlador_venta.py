from Visual.vista_venta import VentanaVenta
from Controlador.controlador_pedido import ControladorPedido

# from Controlador.controlador_vendedor import ControladorVendedor
# from Controlador.controlador_inicio import ControladorInicioSesion

from PyQt6.QtWidgets import *


class ControladorVenta:

    def __init__(self, usuario, id_usuario):
        self.__vista_venta = VentanaVenta(self)
        self.__id_usuario = id_usuario
        # self.__vista_venta.show()
        self.__usuario = usuario
        self.__mesas_ocupadas = set()  # Almacena las mesas ocupadas
        self.__pedido = None  # Para instanciar el controlador del pedido más adelante

        # Guarda las instancias de los pedidos, así no se abren muchas ventanas por mesa
        self.pedidos_activos = {}

    def get_vista(self):
        return self.__vista_venta

    def seleccionar_mesa(self, numero_mesa):
        if numero_mesa in self.pedidos_activos:
            self.__pedido = self.pedidos_activos[numero_mesa]
            self.__pedido.abrir_ventana_pedido()
        else:
            self.__mesas_ocupadas.add(numero_mesa)
            self.__vista_venta.actualizar_estado_mesas(self.__mesas_ocupadas)
            self.__pedido = ControladorPedido(
                self.__id_usuario, numero_mesa, self.actualizar_mesa
            )
            self.pedidos_activos[numero_mesa] = self.__pedido
            self.__pedido.abrir_ventana_pedido()

    def anular_venta(self, numero_mesa):
        if numero_mesa in self.__mesas_ocupadas:
            self.__mesas_ocupadas.remove(numero_mesa)
            self.__vista_venta.actualizar_estado_mesas(self.__mesas_ocupadas)

    def actualizar_mesa(self, numero_mesa, estado):
        if estado == "ocupada":
            self.__mesas_ocupadas.add(numero_mesa)
        elif estado == "libre":
            self.__mesas_ocupadas.remove(numero_mesa)
            if numero_mesa in self.pedidos_activos:
                del self.pedidos_activos[numero_mesa]
        self.__vista_venta.actualizar_estado_mesas(self.__mesas_ocupadas)
