from Visual.vista_cabecera import VistaCabecera
#from vista_ticket import VistaTicket
from Visual.vista_botonera_venta import BotoneraVenta
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys

class VentanaVenta (VistaCabecera):
    
    def __init__(self):
        super().__init__()
        self.boton_venta.setStyleSheet("background-color: rgb(135, 206, 235);")
        
        self.stacked_botones.addWidget(BotoneraVenta())
        #self.stacked_botones.addWidget(VistaTicket())
        self.stacked_botones.setCurrentIndex(0)
        
        self.layout_principal.addLayout(self.stacked_botones)
        
        widget = QWidget()
        widget.setLayout(self.layout_principal)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = VentanaVenta()
window.show()
app.exec()