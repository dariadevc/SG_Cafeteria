from Visual_dos.vista_jefe import VistaJefe
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class VentanaUsuarioJefe (VistaJefe):
    
    def __init__(self,controlador):
        super().__init__(controlador)
        self.setWindowTitle("VentanaUsuarioJefe")
        self.layout_ppal = QHBoxLayout()
        
        ###################################################
        self.tabla_usuarios = QTableWidget()
        self.tabla_usuarios.setColumnCount(6)
        self.tabla_usuarios.setRowCount(8)
        self.tabla_usuarios.setFixedSize(550,450)
        
        self.tabla_usuarios.setItem(1,0,QTableWidgetItem("3423234324"))
        self.tabla_usuarios.setItem(1,1,QTableWidgetItem("fila uno"))
        self.tabla_usuarios.setItem(1,2,QTableWidgetItem("ape1"))
        self.tabla_usuarios.setItem(1,3,QTableWidgetItem("tipo"))
        self.tabla_usuarios.setItem(1,4,QTableWidgetItem("nose"))
        self.tabla_usuarios.setItem(3,0,QTableWidgetItem("12412412"))
        self.tabla_usuarios.setItem(1,1,QTableWidgetItem("olanda"))
        self.tabla_usuarios.setItem(3,2,QTableWidgetItem("qhcace"))
        
        self.tabla_usuarios.setHorizontalHeaderLabels(["DNI","NOMBRE","APELLIDO","TIPO","BAJA","CAUSA"])
        self.tabla_usuarios.verticalHeader().setVisible(False)
        self.tabla_usuarios.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_usuarios.cellClicked.connect(self.selecciono_fila)
        ###################################################
        self.boton_usuario.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.layout_botonera_usuario = QVBoxLayout()
        
        self.boton_refrescar_tabla = QPushButton()
        self.boton_refrescar_tabla.setFixedSize(80,30)
        self.boton_agregar_usuario = QPushButton("AGREGAR USUARIO")
        self.boton_agregar_usuario.setFixedSize(120,70)
        self.boton_modificar_usuario = QPushButton("MODIFICAR USUARIO")
        self.boton_modificar_usuario.setFixedSize(120,70)
        self.boton_eliminar_usuario = QPushButton("ELIMINAR USUARIO")
        self.boton_eliminar_usuario.setFixedSize(120,70)
        
        self.boton_agregar_usuario.clicked.connect(controlador.agregar_usuario)
        self.boton_modificar_usuario.clicked.connect(controlador.modificar_usuario)
        self.boton_eliminar_usuario.clicked.connect(controlador.eliminar_usuario)
        self.boton_refrescar_tabla.clicked.connect(controlador.cargar_usuarios)
        
        self.layout_botonera_usuario.addWidget(self.boton_refrescar_tabla)
        self.layout_botonera_usuario.addWidget(self.boton_agregar_usuario)
        self.layout_botonera_usuario.addWidget(self.boton_modificar_usuario)
        self.layout_botonera_usuario.addWidget(self.boton_eliminar_usuario)
        self.layout_botonera_usuario.setContentsMargins(10,0,0,10)

        self.layout_ppal.addWidget(self.tabla_usuarios)
        self.layout_ppal.addLayout(self.layout_botonera_usuario)
        
        widget_usuario_jefe = QWidget()
        widget_usuario_jefe.setLayout(self.layout_ppal)
        
        self.stacked_layout.addWidget(widget_usuario_jefe)
        self.stacked_layout.setCurrentIndex(1)
    
    def selecciono_fila (self):
        self.tabla_usuarios.selectRow(self.tabla_usuarios.currentRow())
    
    def limpiar_tabla (self):
        self.tabla_usuarios.clearContents()