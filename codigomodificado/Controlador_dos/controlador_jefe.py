from Visual_dos.vista_jefe import VistaJefe
import Controlador_dos.controlador_inicio

class ControladorJefe:
    
    def __init__(self, usuario):
        self.__vista_jefe = VistaJefe(self)
        self.__vista_jefe.show()
        self.__vista_jefe.stack_layout.setCurrentIndex(0)
        self.__vista_jefe.label.setText("Bienvenidoo " + usuario.get_usuario())
    
    def cerrar_sesion (self):
        self.__cerrar = Controlador_dos.controlador_inicio.ControladorInicioSesion()
        self.__vista_jefe.close()
    
    def cambio_a_venta (self):
        self.__vista_jefe.stack_layout.setCurrentIndex(1)
    
    def cambio_a_stock (self):
        self.__vista_jefe.stack_layout.setCurrentIndex(2)