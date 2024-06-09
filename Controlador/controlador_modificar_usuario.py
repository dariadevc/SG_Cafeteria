from Visual.ventana_modificar_usuario import VentanaModificarUsuario
from Modelo.usuario_DAO import UsuarioDAO


class ControladorModificarUsuario:

    def __init__(self, datos_usuario):
        self.__ventana_modificar = VentanaModificarUsuario(self)
        self.__ventana_modificar.label_1.setText(
            f"{self.__ventana_modificar.label_1.text()} {datos_usuario[1]}"
        )
        self.__ventana_modificar.show()
        self.cargar_usuario_a_modificar(datos_usuario)

    def cargar_usuario_a_modificar(self, datos_usuario):
        self.__ventana_modificar.label_dni.setText(f"{datos_usuario[1]}")
        self.__ventana_modificar.input_1.setText(datos_usuario[2])
        self.__ventana_modificar.input_2.setText(datos_usuario[3])
        self.__ventana_modificar.input_3.setText(datos_usuario[5])
        self.__ventana_modificar.input_4.setText(datos_usuario[6])

    def modificar_usuario(self):
        dni_usuario = self.__ventana_modificar.label_dni.text()
        nombre_modificado = self.__ventana_modificar.input_1.text()
        apellido_modificado = self.__ventana_modificar.input_2.text()
        nombre_usuario_modificado = self.__ventana_modificar.input_3.text()
        contrasenia_modificada = self.__ventana_modificar.input_4.text()
        UsuarioDAO().modificar_usuario(
            dni_usuario,
            nombre_modificado,
            apellido_modificado,
            nombre_usuario_modificado,
            contrasenia_modificada,
        )
