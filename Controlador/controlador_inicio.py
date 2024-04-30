from Visual.vista_inicio_sesion import VistaInicioSesion
from Controlador.controlador_jefe import ControladorJefe

class ControladorInicioSesion:
    
    def __init__(self):
        self.__vista = VistaInicioSesion(self)
        self.__vista.show()
    
    def valido_entrada (self):
        nombre = self.__vista.campo_nombre.text()
        contraseña = self.__vista.campo_contraseña.text()
        #if Usuario.validar(nombre, contraseña) == True  
        boolean = True
        if boolean:  ##esto es para probar que se inicie correctamente la siguiente vista
            self.__vista = ControladorJefe()
        else:
            print("Datos Incorrectos")