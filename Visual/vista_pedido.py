from __future__ import annotations
import sys
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class VentanaPedido(QWidget):
    def __init__(self,controlador):
        super().__init__()
        self.setWindowTitle("Pedido")
        self.setFixedSize(675, 500)
        self.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.controlador = controlador
        self._botones_sumar = []
        self._botones_restar = []
        self._etiquetas_cantidad = [] 
        self._productos_agregados= []
        self._pedidos_realizados = []
        

        self._imagenes_x_subido = QPixmap("C://Desktop//SG_Cafeteria//Visual//imagenes//check.jpg").scaled(10, 10)
        self._imagenes_menos_subido = QPixmap("C://SG_Cafeteria//Visual//imagenes//-.jfif").scaled(10, 10)  
        self._imagenes_mas_subido = QPixmap("C://SG_Cafeteria//Visual//imagenes//+.jfif").scaled(10, 10)
        #self._imagenes_x_subido = QPixmap("C://Users//camus//Desktop//SG_Cafeteria//Visual//imagenes//check.jpg").scaled(10, 10)
        #self._imagenes_menos_subido = QPixmap("C://Users//camus//Desktop//SG_Cafeteria//Visual//imagenes//-.jfif").scaled(10, 10)  
        #self._imagenes_mas_subido = QPixmap("C://Users//camus//Desktop//SG_Cafeteria//Visual//imagenes//+.jfif").scaled(10, 10)  
        
        self._contenedor = QVBoxLayout()
        self._contenedor.setSpacing(30)

        self._contenedor_nombres = QHBoxLayout()
        self._etiqueta_comida = QLabel("Comida")
        self._etiqueta_comida.setStyleSheet("background-color: black; color: white;font-weight: bold;")
        self._etiqueta_bebida = QLabel("Bebidas")
        self._etiqueta_bebida.setStyleSheet("background-color: black; color: white;font-weight: bold;")
        self._etiqueta_helado = QLabel("Helados")
        self._etiqueta_helado.setStyleSheet("background-color: black; color: white;font-weight: bold;")

        self._contenedor_nombres.addWidget(self._etiqueta_comida)
        self._contenedor_nombres.addWidget(self._etiqueta_bebida)
        self._contenedor_nombres.addWidget(self._etiqueta_helado)


        self._contenedor.addLayout(self._contenedor_nombres)
        
        
        self._tabla_alta =QHBoxLayout()
        self._tabla_alta.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        self._tabla_comida = QVBoxLayout()
        self._tabla_bebidas = QVBoxLayout()
        self._tabla_helados = QVBoxLayout()

    
        self._tabla_alta.addLayout(self._tabla_comida)
        self._tabla_alta.addLayout(self._tabla_bebidas)
        self._tabla_alta.addLayout(self._tabla_helados)


        self._contenedor.addLayout(self._tabla_alta)
        
        self._tabla_baja = QHBoxLayout()
        self._tabla_baja.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)        

        self._tabla_pedido = QVBoxLayout()   
        _spacio_pedido = QSpacerItem(1000, 600, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self._tabla_pedido.addSpacerItem(_spacio_pedido)

        self._tabla_pedido.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignRight)
        self._boton_cerrar_pedido = QPushButton("Cerrar Pedido")
        font= QFont()
        font.setBold(True)
        self._boton_cerrar_pedido.setFont(font)
        self._tamano_botones = QSize(150,80)
        self._boton_cerrar_pedido.setFixedSize(self._tamano_botones)    
        self._boton_cerrar_pedido.setStyleSheet("background-color: green; color: white")
        self._boton_cerrar_pedido.clicked.connect(controlador.cerrar_pedido)
    
       
        self._tabla_baja.addLayout(self._tabla_pedido)
        self._tabla_baja.addWidget(self._boton_cerrar_pedido)

        
        self._contenedor.addLayout(self._tabla_alta)
        self._contenedor.addLayout(self._tabla_baja)
  
        self.setLayout(self._contenedor)
       

    def agregarFilaConBotones(self, layout, descripcion_producto):
            _fila_layout = QHBoxLayout()
            _tamano_etiqueta = QSize(300, 15)
            _tamano_botones = QSize(15, 15)
            
            _etiqueta_producto = QLabel(descripcion_producto)
            _etiqueta_producto.setFixedSize(_tamano_etiqueta)
            _etiqueta_producto.setFixedWidth(600)
            
            _boton_menos = QPushButton()
            _boton_menos.setFixedSize(_tamano_botones)
            _boton_menos.setIcon(QIcon(self._imagenes_menos_subido))
            _boton_menos.setIconSize(self._imagenes_menos_subido.size())
            _boton_menos.setStyleSheet("background-color: none; padding-top: 7px; padding-bottom: 5px;")
            _boton_menos.setProperty("accion", "restar") 
            _boton_menos.clicked.connect(self.controlador.boton_presionado)
            
            
            _boton_cantidad = QLabel("0")
            _boton_cantidad.setFixedSize(_tamano_botones)
            
            _boton_mas = QPushButton()
            _boton_mas.setFixedSize(_tamano_botones)
            _boton_mas.setIcon(QIcon(self._imagenes_mas_subido))
            _boton_mas.setIconSize(self._imagenes_mas_subido.size())
            _boton_mas.setStyleSheet("background-color: none; padding-top: 7px; padding-bottom: 5px;")
            _boton_mas.setProperty("accion", "sumar")
            _boton_mas.clicked.connect(self.controlador.boton_presionado)
           
        
            _fila_layout.addWidget(_etiqueta_producto)
            _fila_layout.addWidget(_boton_menos)
            _fila_layout.addWidget(_boton_cantidad)
            _fila_layout.addWidget(_boton_mas)           
            layout.addLayout(_fila_layout)
            self._botones_sumar.append(_boton_mas)
            self._botones_restar.append(_boton_menos)
            self._etiquetas_cantidad.append(_boton_cantidad)
            self._productos_agregados.append((_etiqueta_producto.text(), 0))

        
            

    def agregarFilaConBotonEliminar(self, layout, descripcion, precio):
            

        
            _fila_layout = QHBoxLayout()
            __tamano_etiqueta = QSize(200, 15)
            __tamano_botones = QSize(15, 15)
            
            _boton_eliminar = QPushButton()
            _boton_eliminar.setFixedSize(__tamano_botones)
            _boton_eliminar.setIcon(QIcon(self._imagenes_x_subido))
            _boton_eliminar.setIconSize(self._imagenes_x_subido.size())
            _boton_eliminar.setStyleSheet("background-color: none; padding-top: 7px; padding-bottom: 5px;")
            
            
            _etiqueta_descripcion = QLabel(descripcion)
            _etiqueta_descripcion.setFixedSize(__tamano_etiqueta)
            _etiqueta_descripcion.setFixedWidth(300)


            _etiqueta_relleno = QLabel(" X ")
            _etiqueta_relleno.setFixedSize(__tamano_etiqueta)
            _etiqueta_relleno.setFixedWidth(50)

            _etiqueta_cantidad = QLabel("")
            _etiqueta_cantidad.setFixedSize(__tamano_etiqueta)
            _etiqueta_cantidad.setFixedWidth(50)

            _etiqueta_precio = QLabel("$")
            _etiqueta_precio.setFixedSize(__tamano_etiqueta)
            _etiqueta_precio.setFixedWidth(50)

            _precio = QLabel(f'{precio:.2f}')
            _precio.setFixedSize(__tamano_etiqueta)
            _precio.setFixedWidth(50)
            
            _fila_layout.addWidget(_boton_eliminar)
            _fila_layout.addWidget(_etiqueta_descripcion)
            _fila_layout.addWidget(_etiqueta_relleno)
            _fila_layout.addWidget(_etiqueta_cantidad)
            _fila_layout.addWidget(_etiqueta_precio)
            _fila_layout.addWidget(_precio)

            layout.insertLayout(0, _fila_layout)
            return _fila_layout

      

