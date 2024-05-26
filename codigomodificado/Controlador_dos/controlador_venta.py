from Visual_dos.vista_venta_dos import VentanaVenta
from Controlador_dos.controlador_generar_ticket import ControladorTicket
import Controlador_dos.controlador_vendedor
import Controlador_dos.controlador_inicio
from Visual_dos.vista_anular import VistaAnular

from PyQt6.QtWidgets import *

class ControladorVenta:
    
    def __init__(self, usuario):
        self.__vista_venta = VentanaVenta(self)
        #self.__vista_venta.stacked_botones.setCurrentIndex(0)
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
        #self.__vista_venta.boton_anular_venta.setStyleSheet("background-color: lightblue;")
        #self.__vista_venta.boton_generar_ticket.setStyleSheet("background-color: rgb(135, 206, 235);")
        #self.__vista_venta.stacked_botones.setCurrentIndex(1)
        #self.vista_ticket = self.__vista_venta.obtener_vista_ticket()
        #self.controlador_ticket = ControladorTicket(self)
        self.__generar_ticket = ControladorTicket(self.__usuario)
        self.__vista_venta.close()
        #self.__vista_venta.vista_ticket.btn_resta.clicked.connect(self.controlador_ticket.restar_producto)
        #self.__vista_venta.vista_ticket.btn_suma.clicked.connect(self.controlador_ticket.sumar_producto)
        #self.__vista_venta.vista_ticket.btn_imprimir.clicked.connect(self.controlador_ticket.imprimir_producto)
        ##lo que esta arriba es como lo manejamos normalmente ahora
        
        
        ##lo que esta debajo es como deberia ejecutarse todo (preguntar si nos dejan usar stacked layouts como el codigo de
        # arriba, sino implementar clones de VentanaVenta para el generar ticket y anular ventas)
        #self.controlador_ticket = ControladorTicket(vista_ticket)
        #self.__vista_venta.close()
    
    def cambio_a_anular (self):
        print("cambio a anular")
        self.__vista = VistaAnular()
        self.__vista.show()
        #self.__vista_venta.close()
        #self.__vista_venta.boton_generar_ticket.setStyleSheet("background-color: lightblue;")
        #self.__vista_venta.boton_anular_venta.setStyleSheet("background-color: rgb(135, 206, 235);")
        #self.__vista_venta.stacked_botones.setCurrentIndex(1)