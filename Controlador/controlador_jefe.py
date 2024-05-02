from Visual.vista_jefe import VistaJefe

class ControladorJefe:
    
    def __init__(self):
        self.__vista_jefe = VistaJefe(self)
        self.__vista_jefe.show()
        self.__vista_jefe.btn_venta.clicked.connect(self.cambio_a_venta)
        self.__vista_jefe.btn_stock.clicked.connect(self.cambio_a_stock)
    
    def cambio_a_venta (self):
        self.__vista_jefe.stack_layout.setCurrentIndex(0)
    
    def cambio_a_stock (self):
        self.__vista_jefe.stack_layout.setCurrentIndex(1)