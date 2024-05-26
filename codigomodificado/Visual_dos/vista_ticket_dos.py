from Visual_dos.vista_venta_dos import VentanaVenta
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class VistaTicketDos (VentanaVenta):
    
    def __init__(self, controlador):
        super().__init__(controlador)
        
        layout_vertical = QVBoxLayout()
        
        layout_cabecera = QHBoxLayout()
        layout_cabecera.setContentsMargins(170,0,120,0)
        lbl_mesa = QLabel("Nro Mesa")
        lbl_mesa.setFixedSize(100,40)
        qle = QLineEdit()
        qle.setFixedSize(100,30)
        
        layout_cabecera.addWidget(lbl_mesa)
        layout_cabecera.addWidget(qle)
        layout_cabecera.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.layout_mas_menos = QHBoxLayout()
        self.btn_suma = QPushButton("+")
        self.btn_resta = QPushButton("-")
        self.layout_mas_menos.addWidget(self.btn_resta)
        self.layout_mas_menos.addWidget(self.btn_suma)
        self.layout_mas_menos.setContentsMargins(0,0,0,0)
        self.layout_mas_menos.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        layout_tablas = QHBoxLayout()
        
        self.tabla1 = QTableWidget()
        self.tabla1.setColumnCount(2)
        #self.tabla1.setRowCount(20)
        self.tabla1.verticalHeader().setVisible(False)
        self.tabla1.horizontalHeader().setVisible(False)
        self.tabla1.setColumnWidth(0,200)
        self.tabla1.setColumnWidth(1,65)
        
        self.tabla2 = QTableWidget()
        self.tabla2.setColumnCount(2)
        self.tabla2.setRowCount(0)  # Inicialmente vacía
        self.tabla2.verticalHeader().setVisible(False)
        self.tabla2.horizontalHeader().setVisible(False)
        self.tabla2.setColumnWidth(0, 200)
        self.tabla2.setColumnWidth(1, 65)

        layout_tablas.addWidget(self.tabla1)
        layout_tablas.addWidget(self.tabla2)
        
        layout_imprimir = QHBoxLayout()
        self.btn_imprimir = QPushButton("IMPRIMIR")
        self.btn_imprimir.setFixedSize(250,40)
        self.btn_imprimir.setStyleSheet('background-color: lightblue')
        self.btn_imprimir.setContentsMargins(0,20,0,0)
        
        layout_imprimir.addWidget(self.btn_imprimir)
        
        layout_vertical.addLayout(layout_cabecera)
        layout_vertical.addLayout(self.layout_mas_menos)
        layout_vertical.addLayout(layout_tablas)
        layout_vertical.addLayout(layout_imprimir)
        layout_vertical.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        layout_vertical.setContentsMargins(10,10,10,10)
        
        self.contenedor.setLayout(layout_vertical)
        
        self.btn_suma.clicked.connect(controlador.sumar_producto)
        self.btn_resta.clicked.connect(controlador.restar_producto)
        self.btn_imprimir.clicked.connect(controlador.imprimir_producto)
        self.boton_cerrar.clicked.connect(controlador.cerrar_sesion)
        self.boton_stock.clicked.connect(controlador.cambio_a_stock)
        self.boton_informe.clicked.connect(controlador.cambio_a_informe)
        self.boton_generar_ticket.clicked.connect(controlador.cambio_a_generar)
        self.boton_anular_venta.clicked.connect(controlador.cambio_a_anular)
        