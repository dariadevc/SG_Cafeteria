from Visual.ventana_eliminar_usuario import VentanaEliminarUsuario
from Modelo.usuario_DAO import UsuarioDAO


class ControladorEliminarUsuario:

    def __init__(self, dni_usuario):
        self.__ventana_eliminar = VentanaEliminarUsuario(self)
        self.__ventana_eliminar.show()
        self.__dni_usuario = dni_usuario

    def eliminar_usuario(self):
        usuario_dao = UsuarioDAO()
        causa = self.__ventana_eliminar.combo_box.currentText()
        usuario_dao.eliminar_usuario(self.__dni_usuario, causa)
        self.__ventana_eliminar.notifico_eliminacion(self.__dni_usuario, causa)
        self.__ventana_eliminar.hide()
