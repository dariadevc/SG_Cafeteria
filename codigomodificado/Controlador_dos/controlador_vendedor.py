from Visual_dos.vista_vendedor_2 import VistaVendedor
from Controlador_dos.controlador_venta import ControladorVenta
import Controlador_dos.controlador_inicio

class ControladorVendedor:
    
    def __init__(self, usuario):
        self.__vista_vendedor = VistaVendedor()
        self.__vista_vendedor.show()
        self._usuario = usuario
        nombre_usuario = usuario.get_usuario()
        self.__vista_vendedor.label.setText(nombre_usuario)
        self.__vista_vendedor.btn_cerrar.clicked.connect(self.logout)
        self.__vista_vendedor.boton_venta.clicked.connect(self.cambio_a_venta)
        self.__vista_vendedor.boton_stock.clicked.connect(self.cambio_a_stock)
        self.__vista_vendedor.boton_informe.clicked.connect(self.cambio_a_informe)
    
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