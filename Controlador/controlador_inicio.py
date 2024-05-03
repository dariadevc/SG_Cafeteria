from Visual.vista_inicio_sesion import VistaInicioSesion
from Controlador.controlador_jefe import ControladorJefe
from Modelo.usuario import Usuario

class ControladorInicioSesion:
    
    def __init__(self):
        self.__vista = VistaInicioSesion(self)
        self.__vista.show()
    
    def valido_entrada (self):
        nombre = self.__vista.campo_nombre.text()
        contraseña = self.__vista.campo_contraseña.text()
        tipo = self.__vista.combo_1.currentText()
        usuario = Usuario('','','',tipo,nombre,contraseña,'','')
        
        if usuario.login() != None:  ##esto es para probar que se inicie correctamente la siguiente vista
            self.__vista.estado.hide()
            self.__vista = ControladorJefe(usuario)
        else:
            self.__vista.estado.show()