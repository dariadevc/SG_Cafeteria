from Visual_dos.vista_venta import VentanaVenta
from Controlador_dos.controlador_generar_ticket import ControladorTicket
import Controlador_dos.controlador_vendedor
import Controlador_dos.controlador_inicio
from Visual_dos.vista_anular import VistaAnular

from PyQt6.QtWidgets import *

class ControladorVenta:
    
    def __init__(self, usuario):
        self.__vista_venta = VentanaVenta(self)
        self.__vista_venta.show()
        self.__usuario = usuario
        nombre_usuario = usuario.get_usuario()        
        self.__vista_venta.label.setText(nombre_usuario)

    def cerrar_sesion (self):
        self.__cerrar = Controlador_dos.controlador_inicio.ControladorInicioSesion()
        self.__vista_venta.close()

    def cambio_a_stock (self):
        self.__vendedor_stock = Controlador_dos.controlador_vendedor.ControladorVendedor(self.__usuario).cambio_a_stock()
        self.__vista_venta.close()
    
    def cambio_a_informe (self):
        self.__vendedor_informe = Controlador_dos.controlador_vendedor.ControladorVendedor(self.__usuario).cambio_a_informe()
        self.__vista_venta.close()
    
    def cambio_a_generar (self):
        self.__generar_ticket = ControladorTicket(self.__usuario)
        #self.__vista_venta.close()
    
    def cambio_a_anular (self):
        print("cambio a anular")
        self.__vista = VistaAnular()
        self.__vista.show()
        #self.__vista_venta.close()