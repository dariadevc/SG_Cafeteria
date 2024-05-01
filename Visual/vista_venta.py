from PyQt6.QtWidgets import *

class VistaVenta (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #637d96")
        #self.setStyleSheet("background-color: #1f3e53")
        layout = QHBoxLayout()
        
        tabla = QTableWidget()
        tabla.setColumnCount(6)
        tabla.setRowCount(30)
        
        ################PARTE DERECHA DE LA PAGINA#####################
        layout_vertical = QVBoxLayout()
        
        #############################BUSQUEDA#######################
        layout_busqueda = QHBoxLayout()
        barra_busqueda = QLineEdit()
        btn_busqueda = QPushButton("Buscar")
        btn_busqueda.setStyleSheet("background-color: #36536a")
        
        layout_busqueda.addWidget(barra_busqueda)
        layout_busqueda.addWidget(btn_busqueda)
        ############################BUSQUEDA########################
        
        btn_suspender = QPushButton("Suspender Venta")
        btn_suspender.setStyleSheet("background-color: #36536a")
        btn_registrar = QPushButton("Registrar Venta")
        btn_registrar.setStyleSheet("background-color: #36536a")
        
        layout_vertical.addLayout(layout_busqueda)
        layout_vertical.addWidget(btn_suspender)
        layout_vertical.addWidget(btn_registrar)
        
        layout.addWidget(tabla)
        layout.addLayout(layout_vertical)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)