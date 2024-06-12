from Visual.ventana_usuario_jefe import VentanaUsuarioJefe
from Modelo.usuario_DAO import UsuarioDAO
from Controlador.controlador_agregar_usuarios import ControladorAgregarUsuario
from Controlador.controlador_eliminar_usuarios import ControladorEliminarUsuario
from Controlador.controlador_modificar_usuario import ControladorModificarUsuario
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class ControladorJefeUsuario:

    def __init__(self):
        self.__ventana_usuario_jefe = VentanaUsuarioJefe(self)
        self.__ventana_usuario_jefe.show()
        self.__usuario_dao = UsuarioDAO()
        self.cargar_usuarios()

    def cargar_usuarios(self):
        self.__ventana_usuario_jefe.limpiar_tabla()
        usuarios = self.__usuario_dao.obtener_todos_usuarios(0)
        self.__ventana_usuario_jefe.tabla_usuarios.setRowCount(len(usuarios))
        for fila, usuario in enumerate(usuarios):
            dni = QTableWidgetItem(f"{usuario[1]}")
            nombre = QTableWidgetItem(f"{usuario[2]}")
            apellido = QTableWidgetItem(f"{usuario[3]}")
            tipo = QTableWidgetItem(f"{usuario[4]}")
            baja = QTableWidgetItem(f"{usuario[7]}")
            causa = QTableWidgetItem(f"{usuario[8]}")

            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila, 0, dni)
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila, 1, nombre)
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila, 2, apellido)
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila, 3, tipo)
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila, 4, baja)
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila, 5, causa)

    def get_vista(self):
        return self.__ventana_usuario_jefe

    def agregar_usuario(self):
        self.__controlador_agregar = ControladorAgregarUsuario()

    def modificar_usuario(self):
        try:
            usuario_seleccionado = (
                self.__ventana_usuario_jefe.tabla_usuarios.selectedItems()
            )
            usuario_a_modificar = self.__usuario_dao.obtener_un_usuario(
                usuario_seleccionado[0].text()
            )
            self.__controlador_modificar = ControladorModificarUsuario(
                usuario_a_modificar
            )
        except IndexError:
            self.__ventana_usuario_jefe.boton_modificar_usuario.setStyleSheet(
                "background-color:gray"
            )
            QTimer.singleShot(1000, self.cambio_de_color)

    def eliminar_usuario(self):
        try:
            usuario_seleccionado = (
                self.__ventana_usuario_jefe.tabla_usuarios.selectedItems()
            )
            self.__controlador_eliminar = ControladorEliminarUsuario(
                usuario_seleccionado[0].text()
            )
        except IndexError:
            self.__ventana_usuario_jefe.boton_eliminar_usuario.setStyleSheet(
                "background-color:gray"
            )
            QTimer.singleShot(1000, self.cambio_de_color)

    def cambio_de_color(self):
        self.__ventana_usuario_jefe.boton_eliminar_usuario.setStyleSheet(
            "background-color: rgb(135, 206, 235)"
        )
        self.__ventana_usuario_jefe.boton_modificar_usuario.setStyleSheet(
            "background-color: rgb(135, 206, 235)"
        )
