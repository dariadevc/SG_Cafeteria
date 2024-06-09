from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class VentanaUsuarioJefe (QWidget):
    
    def __init__(self):
        super().__init__()
        self.layout_ppal = QHBoxLayout()
        
        ###################################################
        self.tabla_usuarios = QTableWidget()
        self.tabla_usuarios.setColumnCount(6)
        self.tabla_usuarios.setColumnWidth(0,100)
        self.tabla_usuarios.setColumnWidth(3,80)
        self.tabla_usuarios.setColumnWidth(4,150)
        self.tabla_usuarios.setColumnWidth(5,50)
        self.tabla_usuarios.setFixedSize(550,450)
        
        self.tabla_usuarios.setHorizontalHeaderLabels(["DNI","NOMBRE","APELLIDO","NOMBRE USUARIO","CAUSA","BAJA"])
        self.tabla_usuarios.verticalHeader().setVisible(False)
        self.tabla_usuarios.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.tabla_usuarios.setStyleSheet("background-color: white;")
        self.tabla_usuarios.horizontalHeader().setStyleSheet(
            "background-color: lightblue; font-weight: bold;"
        )

        self.tabla_usuarios.cellClicked.connect(self.selecciono_fila)
        ###################################################
        self.layout_botonera_usuario = QVBoxLayout()
        
        self.boton_refrescar_tabla = QPushButton()
        self.boton_refrescar_tabla.setFixedSize(80,30)
        self.boton_agregar_usuario = QPushButton("AGREGAR USUARIO")
        self.boton_agregar_usuario.setFixedSize(120,70)
        self.boton_modificar_usuario = QPushButton("MODIFICAR USUARIO")
        self.boton_modificar_usuario.setFixedSize(120,70)
        self.boton_eliminar_usuario = QPushButton("ELIMINAR USUARIO")
        self.boton_eliminar_usuario.setFixedSize(120,70)
        
        # self.boton_agregar_usuario.clicked.connect(controlador.agregar_usuario)
        # self.boton_modificar_usuario.clicked.connect(controlador.modificar_usuario)
        # self.boton_eliminar_usuario.clicked.connect(controlador.eliminar_usuario)
        # self.boton_refrescar_tabla.clicked.connect(controlador.cargar_usuarios)
        
        self.layout_botonera_usuario.addWidget(self.boton_refrescar_tabla)
        self.layout_botonera_usuario.addWidget(self.boton_agregar_usuario)
        self.layout_botonera_usuario.addWidget(self.boton_modificar_usuario)
        self.layout_botonera_usuario.addWidget(self.boton_eliminar_usuario)
        self.layout_botonera_usuario.setContentsMargins(10,0,0,10)

        self.layout_ppal.addWidget(self.tabla_usuarios)
        self.layout_ppal.addLayout(self.layout_botonera_usuario)
        
        self.setLayout(self.layout_ppal)
    
    def selecciono_fila (self):
        self.tabla_usuarios.selectRow(self.tabla_usuarios.currentRow())
    
    def limpiar_tabla (self):
        self.tabla_usuarios.clearContents()