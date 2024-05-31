from Visual_dos.ventana_agregar_usuario import VentanaAgregarUsuario
from Modelo_dos.usuario import Usuario

class ControladorAgregarUsuario:
    
    def __init__(self):
        self.__ventana_agregar_usuario = VentanaAgregarUsuario(self)
        self.__ventana_agregar_usuario.show()
    
    def agregar_usuario_a_bd (self):
        dni = int(self.__ventana_agregar_usuario.line_edit_1.text())
        nombre = self.__ventana_agregar_usuario.line_edit_2.text()
        apellido = self.__ventana_agregar_usuario.line_edit_3.text()
        nombre_usuario = self.__ventana_agregar_usuario.line_edit_4.text()
        contrasenia = self.__ventana_agregar_usuario.line_edit_5.text()
        usuario_nuevo = Usuario(dni, nombre, apellido, '', nombre_usuario, contrasenia,'','')
        usuario_nuevo.agregar_a_bd()
        #print("Usuario agregado correctamente")