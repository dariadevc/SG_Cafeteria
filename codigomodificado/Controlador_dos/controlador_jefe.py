from Visual_dos.vista_jefe import VistaJefe
from Controlador_dos.controlador_jefe_usuario import ControladorJefeUsuario
import Controlador_dos.controlador_inicio


class ControladorJefe:
    
    def __init__(self, usuario):
        self.__vista_jefe = VistaJefe(self)
        self.__vista_jefe.show()
        self._usuario = usuario
        self.__vista_jefe.label.setText("Bienvenidoo Jefe " + usuario.get_usuario())
    
    def cerrar_sesion (self):
        self.__cerrar = Controlador_dos.controlador_inicio.ControladorInicioSesion()
        self.__vista_jefe.close()
    
    def cambio_a_venta (self):
        print("venta jefe")
        #self.__ventana_jefe_venta = ControladorJefeVenta(self._usuario)
        #self.__vista_jefe.close()
    
    def cambio_a_stock (self):
        print("stock jefe")
        #self.__ventana_jefe_stock = ControladorJefeStock(self._usuario)
        #self.__vista_jefe.close()
    
    def cambio_a_informe (self):
        print("informe jefe")
        #self.__ventana_jefe_informe = ControladorJefeInforme(self._usuario)
        #self.__vista_jefe.close()
    
    def cambio_a_usuario (self):
        self.__ventana_jefe_usuario = ControladorJefeUsuario(self._usuario)
        self.__vista_jefe.close()