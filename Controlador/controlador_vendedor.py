from Visual.vista_vendedor_2 import VistaVendedor
from Controlador.controlador_venta import ControladorVenta

class ControladorVendedor:
    
    def __init__(self, usuario):
        self.__vista_vendedor = VistaVendedor()
        self.__vista_vendedor.show()
        self._usuario = usuario.get_usuario()
        self.__vista_vendedor.label.setText(self._usuario)
        self.__vista_vendedor.boton_venta.clicked.connect(self.cambio_a_venta)
        self.__vista_vendedor.boton_stock.clicked.connect(self.cambio_a_stock)
        self.__vista_vendedor.boton_informe.clicked.connect(self.cambio_a_informe)
    
    def cambio_a_venta (self):
        self.__vista_vendedor = ControladorVenta(self._usuario)
    
    def cambio_a_stock (self):
        print("stock click")
    
    def cambio_a_informe (self):
        print("informe click")