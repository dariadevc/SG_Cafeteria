from Visual.vista_jefe import VistaJefe

class ControladorJefe:
    
    def __init__(self):
        self.__vista_jefe = VistaJefe(self)
        self.__vista_jefe.show()
        self.__vista_jefe.btn_venta.clicked.connect(self.cambio_a_venta)
    
    def cambio_a_venta (self):
        self.__vista_jefe.stack_layout.setCurrentIndex(0)