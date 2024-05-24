from Visual.vista_venta_dos import VentanaVenta

class ControladorVenta:
    
    def __init__(self, usuario):
        self.__vista_venta = VentanaVenta()
        self.__vista_venta.stacked_botones.setCurrentIndex(0)
        self.__vista_venta.show()
        self.usuario = usuario
        self.__vista_venta.label.setText(self.usuario)
        self.__vista_venta.boton_stock.clicked.connect(self.cambio_a_stock)
        self.__vista_venta.boton_informe.clicked.connect(self.cambio_a_informe)
        self.__vista_venta.boton_generar_ticket.clicked.connect(self.cambio_a_generar)
        self.__vista_venta.boton_anular_venta.clicked.connect(self.cambio_a_anular)
    
    
    def cambio_a_stock (self):
        print("stock click")
    
    def cambio_a_informe (self):
        print("informe click")
    
    def cambio_a_generar (self):
        self.__vista_venta.boton_anular_venta.setStyleSheet("background-color: lightblue;")
        self.__vista_venta.boton_generar_ticket.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.__vista_venta.stacked_botones.setCurrentIndex(1)
    
    def cambio_a_anular (self):
        self.__vista_venta.boton_generar_ticket.setStyleSheet("background-color: lightblue;")
        self.__vista_venta.boton_anular_venta.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.__vista_venta.stacked_botones.setCurrentIndex(2)