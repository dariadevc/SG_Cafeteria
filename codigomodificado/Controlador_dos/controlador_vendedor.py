from Visual_dos.vista_vendedor import VistaVendedor
from Controlador_dos.controlador_venta import ControladorVenta
import Controlador_dos.controlador_inicio

class ControladorVendedor:
    
    def __init__(self, usuario):
        self.__vista_vendedor = VistaVendedor(self)
        self.__vista_vendedor.show()
        self._usuario = usuario
        nombre_usuario = usuario.get_usuario()
        self.__vista_vendedor.label.setText(nombre_usuario)
    
    def cambio_a_venta (self):
        self.__vista_venta = ControladorVenta(self._usuario)
        self.__vista_vendedor.close()
    
    def cambio_a_stock (self):
        print("stock click")
    
    def cambio_a_informe (self):
        print("informe click")
    
    def logout (self):
        self.__vista_inicio = Controlador_dos.controlador_inicio.ControladorInicioSesion()
        self.__vista_vendedor.close()