from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
# sys.path.append('C://Users//camus//Desktop//SG_Cafeteria//Visual')
# sys.path.append('C://Users//camus//Desktop//SG_Cafeteria//Controlador')
# sys.path.append('C://Users//camus//Desktop//SG_Cafeteria//Modelo')

from Visual_dos.vista_inicio_sesion import VistaInicioSesion
from Controlador_dos.controlador_vendedor import ControladorVendedor
from Controlador_dos.controlador_jefe import ControladorJefe
from Modelo_dos.usuario import Usuario

class ControladorInicioSesion:

    def __init__(self):
        self.__vista = VistaInicioSesion(self)
        self.__vista.show()
    
    def cambio_modo_contrasena(self):
        if self.__vista.contrasena_oculta:
            self.__vista.imagen_contrasena.setIcon(QIcon(self.__vista.imagen_contrasena_visible))
            self.__vista.imagen_contrasena.setIconSize(self.__vista.imagen_contrasena_visible.size())
            self.__vista.inputContrasenia.setEchoMode(QLineEdit.EchoMode.Normal)  
        else:
            self.__vista.imagen_contrasena.setIcon(QIcon(self.__vista.imagen_contrasena_oculta))
            self.__vista.imagen_contrasena.setIconSize(self.__vista.imagen_contrasena_oculta.size())
            self.__vista.inputContrasenia.setEchoMode(QLineEdit.EchoMode.Password)  
        
        self.__vista.contrasena_oculta = not self.__vista.contrasena_oculta # Cambia el estado
    
    def valido_entrada(self):
        nombre_usuario = self.__vista.inputUsuario.text()
        contrasenia = self.__vista.inputContrasenia.text()
        
        tipo = "VENDEDOR"
        usuario = Usuario('','','',tipo,nombre_usuario,contrasenia,'','')
        
        if usuario.login() is not None:
            if tipo == "VENDEDOR":
                self.inicio = ControladorVendedor(usuario)
            else:
                self.inicio = ControladorJefe(usuario)
            self.__vista.close()
        else:
            self.__vista.etiqueta_error.setText('Usuario o contrasena Incorrecta') 
            QTimer.singleShot(2000, self.limpiar_error)
    
    def limpiar_error(self):
        self.__vista.etiqueta_error.setText(" ")