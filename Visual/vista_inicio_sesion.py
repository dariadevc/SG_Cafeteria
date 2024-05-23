import sys
from PyQt6.QtCore import * 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *




class VistaInicioSesion(QMainWindow):
    def __init__(self,controlador):
        super().__init__()
        self.setWindowTitle("Bienvenido ")
        self.setFixedSize(QSize(400, 500))            
      
        palette = QPalette()
        palette.setColor(QPalette.ColorGroup.All, QPalette.ColorRole.Window, QColor(135, 206, 235)) #color de la ventana
        self.setPalette(palette)
        
        self.contenedor_principal = QVBoxLayout() 
        self.frame_imagen = QFrame()
        self.frame_login = QFrame()
        self.contenedor_vertical = QVBoxLayout(self.frame_login)  
        self.contenedor_vertical.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)


        self.contenedor_horizontal= QHBoxLayout(self.frame_imagen) #para almacenar la las etiquetas de imagen y nombre empresa
        self.contenedor_horizontal.setContentsMargins(0, 0, 0, 0)
       # self.contenedor_horizontal.setSpacing(0) 
        self.contenedor_horizontal.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
  
        self.etiqueta_cafe = QLabel()
       # self.etiqueta_cafe.setContentsMargins(0, 0, 0, 0)     
        self.imagen= QPixmap("C://Users//camus//Desktop//SG_Cafeteria//Visual//imagenes//coffe.png").scaled(25, 25)  
        self.etiqueta_cafe.setPixmap(self.imagen)
        self.etiqueta_nombre = QLabel(" Cafe Viera",self)
        #self.etiqueta_nombre.setContentsMargins(0, 0, 0, 0)
        self.etiqueta_nombre.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.etiqueta_nombre.setStyleSheet("color: white; font-weight: bold; font-size: 20px")
        self.contenedor_horizontal.addWidget(self.etiqueta_cafe)
        self.contenedor_horizontal.addWidget(self.etiqueta_nombre)
        
   
      
        lblIniciarSesion = QLabel("Iniciar Sesion")
        lblIniciarSesion.setStyleSheet("color: white; font-weight: bold; font-size: 20px; margin-left: 50px")
        self.contenedor_vertical.addWidget(lblIniciarSesion)
        self.contenedor_vertical.addSpacing(20)
        lblUsuario = QLabel("Usuario") 
        lblUsuario.setStyleSheet("color: white; font-weight: bold; font-size: 16px; margin-left: 5px")
        self.contenedor_vertical.addWidget(lblUsuario)
        self.contenedor_vertical.addSpacing(20)
        self.inputUsuario = QLineEdit("kelly64")
        self.inputUsuario.setStyleSheet("margin-left: 30px")
        self.inputUsuario.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.inputUsuario.setFixedWidth(200)    
        self.contenedor_vertical.addWidget(self.inputUsuario)
        self.contenedor_vertical.addSpacing(20)
        lblConstrasenia = QLabel("Contraseña")
        lblConstrasenia.setStyleSheet("color: white; font-weight: bold; font-size: 16px; margin-left: 5px")
        self.contenedor_vertical.addWidget(lblConstrasenia)
        self.contenedor_vertical.addSpacing(20)  
        self.frame_contrasena = QFrame()
        self.contenedor_contrasena = QHBoxLayout(self.frame_contrasena)
        self.contenedor_contrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.inputContrasenia = QLineEdit('s6BJseOY%)')
        self.inputContrasenia.setEchoMode(QLineEdit.EchoMode.Password)
        self.inputUsuario.setStyleSheet("margin-left: 3px")
        self.inputContrasenia.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.inputContrasenia.setFixedWidth(200)
        self.inputContrasenia.setFixedHeight(21)
        self.contenedor_contrasena.addWidget(self.inputContrasenia)

        self.imagen_contrasena = QPushButton()    #boton contrasena oculta  
        self.imagen_contrasena.setFixedSize(27, 25)   
        self.imagen_contrasena_oculta= QPixmap("C://Users//camus//Desktop//SG_Cafeteria//Visual//imagenes//contrasena_oculta").scaled(30, 25)  
        self.imagen_contrasena_visible= QPixmap("C://Users//camus//Desktop//SG_Cafeteria//Visual//imagenes////contrasena_visible").scaled(30, 25) 
        self.imagen_contrasena.setIcon(QIcon(self.imagen_contrasena_oculta))
        self.imagen_contrasena.setIconSize(self.imagen_contrasena_oculta.size())
        self.imagen_contrasena.setStyleSheet("background-color: none; padding-top: 7px; padding-bottom: 5px;")
        self.imagen_contrasena.pressed.connect(controlador.cambio_modo_contrasena)
        self.contrasena_oculta = True
      
        
        
        self.contenedor_contrasena.addWidget(self.imagen_contrasena)
        self.contenedor_vertical.addWidget(self.frame_contrasena)
        self.contenedor_vertical.addSpacing(20)
        self.iniciar_sesion = QPushButton("Ingresar")
        self.iniciar_sesion.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.iniciar_sesion.setFixedWidth(160)
        self.iniciar_sesion.setFixedHeight(40)
        self.iniciar_sesion.setStyleSheet("margin-left: 80px;") 
        self.contenedor_vertical.addWidget(self.iniciar_sesion)
        self.iniciar_sesion.pressed.connect(controlador.valido_entrada)
        self.contenedor_vertical.addSpacing(20)
        self.etiqueta_error = QLabel("")
        self.etiqueta_error.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.etiqueta_error.setStyleSheet("background-color: bold; color: red;")
        self.contenedor_vertical.addWidget(self.etiqueta_error)
        
        
        
        self.contenedor_principal.addWidget(self.frame_imagen)   
        self.contenedor_principal.addWidget(self.frame_login)   
        central_widget = QWidget()  
        central_widget.setLayout(self.contenedor_principal)
        self.setCentralWidget(central_widget)  