from __future__ import annotations
from Modelo.usuario_DAO import UsuarioDAO


class Usuario:
    def __init__(self, dni, nombre, apellido, tipo, usuario, contra, baja, causa):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tipo = tipo
        self.__usuario = usuario
        self.__contra = contra
        self.__baja = baja
        self.__causa = causa
        self.__usuariodao = UsuarioDAO()

    ## Getters y Setters

    def get_dni(self):
        print("Se solicitó el dni del usuario.")
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni
        print("Se modificó el dni del usuario.")

    def get_nombre(self):
        print("Se solicitó el nombre del usuario.")
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
        print("Se modificó el nombre del usuario.")

    def get_apellido(self):
        print("Se solicitó el apellido del usuario.")
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido
        print("Se modificó el apellido del usuario.")

    def get_tipo(self):
        print("Se solicitó el tipo del usuario.")
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo
        print("Se modificó el tipo del usuario.")

    def get_usuario(self):
        print("Se solicitó el usuario del usuario.")
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario
        print("Se modificó el usuario del usuario.")

    def get_contra(self):
        print("Se solicitó el contra del usuario.")
        return self.__contra

    def set_contra(self, contra):
        self.__contra = contra
        print("Se modificó el contra del usuario.")

    def get_baja(self):
        print("Se solicitó el baja del usuario.")
        return self.__baja

    def set_baja(self, baja):
        self.__baja = baja
        print("Se modificó el baja del usuario.")

    def get_causa(self):
        print("Se solicitó el causa del usuario.")
        return self.__causa

    def set_causa(self, causa):
        self.__causa = causa
        print("Se modificó el causa del usuario.")

    def datos_usuario(self):
        datos = f"DNI: {self.__dni} | NOMBRE: {self.__nombre} | APELLIDO: {self.__apellido} | TIPO: {self.__tipo} | USUARIO: {self.__usuario}"
        if self.__baja == False:
            return datos
        else:
            return datos + f" | BAJA: {self.__baja} | CAUSA: {self.__causa}"

    def login(self):
        result = self.__usuariodao.login_usuario(self.__usuario, self.__contra)
        return result
