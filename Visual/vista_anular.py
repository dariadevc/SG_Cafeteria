from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class VistaAnular (QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        lbl_bienvenida = QLabel("Bienvenido a Anular Venta!!!")
        
        tabla = QTableWidget()
        
        
        layout.addWidget(lbl_bienvenida)
        layout.addWidget(tabla)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)