from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

class VistaTicket(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        layout_vertical = QVBoxLayout()
        #########################################################
        layout_cabecera = QHBoxLayout()
        layout_cabecera.setContentsMargins(170,0,120,100)
        lbl_mesa = QLabel("Nro Mesa")
        lbl_mesa.setFixedSize(100,40)
        #lbl_mesa.setStyleSheet("background-color: yellow;")
        qle = QLineEdit()
        qle.setFixedSize(100,40)
        #qle.setStyleSheet("background-color: pink;")
        layout_cabecera.addWidget(lbl_mesa)
        layout_cabecera.addWidget(qle)
        
        btn_imprimir = QPushButton("IMPRIMIR")
        btn_imprimir.setFixedSize(250,40)
        btn_imprimir.setStyleSheet('background-color: lightblue')
        
        layout_vertical.addLayout(layout_cabecera)
        layout_vertical.addWidget(btn_imprimir)
        
        widget = QWidget()
        widget.setLayout(layout_vertical)
        self.setCentralWidget(widget)