from Visual.ventana_agregar_usuario import VentanaAgregarUsuario
from Modelo.usuario import Usuario


class ControladorAgregarUsuario:

    def __init__(self):
        self.__ventana_agregar_usuario = VentanaAgregarUsuario(self)
        self.__ventana_agregar_usuario.show()

    def agregar_usuario_a_bd(self):
        try:
            dni = int(self.__ventana_agregar_usuario.line_edit_1.text())
            nombre = self.__ventana_agregar_usuario.line_edit_2.text()
            apellido = self.__ventana_agregar_usuario.line_edit_3.text()
            nombre_usuario = self.__ventana_agregar_usuario.line_edit_4.text()
            contrasenia = self.__ventana_agregar_usuario.line_edit_5.text()
            datos_a_comparar = [dni, nombre, apellido, nombre_usuario, contrasenia]
            if None in datos_a_comparar or '' in datos_a_comparar:
                raise ValueError
            else:
                datos_validados = ["",dni,nombre,apellido,nombre_usuario,contrasenia,"","",""]
                usuario_nuevo = Usuario(datos_validados)
                usuario_nuevo.agregar_a_bd()
                self.__ventana_agregar_usuario.notifico_insercion(dni)
                self.__ventana_agregar_usuario.hide()
        except:
            self.__ventana_agregar_usuario.imprimo_alerta()