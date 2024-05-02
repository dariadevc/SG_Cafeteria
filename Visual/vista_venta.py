from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class VistaVenta (QMainWindow):
    
    def __init__(self):
        super().__init__()
        #self.setStyleSheet("background-color: #637d96")
        self.setStyleSheet("background-color: #1f3e53")
        self.setFixedSize(600,400)
        self.setMaximumSize(600,400)
        self.setMinimumSize(600,400)
        layout = QHBoxLayout()
        
        tabla = QTableWidget()
        tabla.setColumnCount(4)
        tabla.setRowCount(10)
        tabla.setFixedSize(400,380)
        ################PARTE DERECHA DE LA PAGINA#####################
        layout_vertical = QVBoxLayout()
        
        #############################BUSQUEDA#######################
        layout_busqueda = QHBoxLayout()
        layout_busqueda.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_busqueda.setContentsMargins(4,100,4,-1)
        barra_busqueda = QLineEdit()
        barra_busqueda.setFixedSize(100,30)

        btn_busqueda = QPushButton("Buscar")
        btn_busqueda.setFixedSize(60,30)
        btn_busqueda.setStyleSheet("background-color: #36536a")
        
        layout_busqueda.addWidget(barra_busqueda)
        layout_busqueda.addWidget(btn_busqueda)
        ############################BUSQUEDA########################

        layout_botones = QVBoxLayout()
        btn_suspender = QPushButton("Suspender Venta")
        btn_suspender.setStyleSheet("background-color: #36536a")
        btn_suspender.setFixedSize(90,30)

        btn_registrar = QPushButton("Registrar Venta")
        btn_registrar.setStyleSheet("background-color: #36536a")
        btn_registrar.setFixedSize(90,30)

        layout_botones.addWidget(btn_suspender)
        layout_botones.addWidget(btn_registrar)
        layout_botones.setContentsMargins(4,0,4,120)
        layout_botones.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_vertical.addLayout(layout_busqueda)
        layout_vertical.addLayout(layout_botones)

        layout.addWidget(tabla)
        layout.addLayout(layout_vertical)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)