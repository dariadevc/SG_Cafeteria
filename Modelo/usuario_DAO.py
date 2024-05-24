# from __future__ import annotations
import sys
#sys.path.append('C://Users//camus//Desktop//SG_Cafeteria//Modelo')
from Modelo.base_de_datos import BaseDeDatos

# from usuario import Usuario


class UsuarioDAO:
    def __init__(self):
        self.base = BaseDeDatos()

    def login_usuario(self, usuario, contra):
        consulta = f"SELECT * FROM public.usuarios WHERE nombre_usuario = '{usuario}' and contra = '{contra}';"
        return self.base.obtener_un_elemento(consulta)

    def agregar_usuario(self, dni, nombre, apellido, usuario, contra):
        consulta = 'INSERT into public."usuarios"(dni_empleado, nombre_empleado, apellido_empleado, nombre_usuario, contra) VALUES (%s, %s, %s, %s, %s);'
        valores = (dni, nombre, apellido, usuario, contra)
        self.base.consulta(consulta, valores)
        print(f"Se agrego a la base de datos un usuario con el dni {dni}")

    def eliminar_usuario(self, dni, causa):
        consulta = 'UPDATE public."usuarios" SET usuario_eliminado = %s, causa_eliminacion = %s WHERE dni_empleado = %s;'
        valores = (True, causa, dni)
        self.base.consulta(consulta, valores)
        print(f"Se dio la baja lógica del usuario con el dni {dni}")

    ## TODO: Agregar los "usuario_modificado.get_[x]" cuando los defina.
    def modificar_usuario(self, dni):  # , usuario_modificado=Usuario):
        consulta = 'UPDATE public."usuarios" SET dni_empleado = %s, nombre_empleado = %s, apellido_empleado = %s, nombre_usuario = %s, contra = %s WHERE dni_empleado = %s;'
        valores = ()
        self.base.consulta(consulta, valores)
        print(f"Se modificaron los datos del usuario con el dni {dni}")

    def obtener_un_usuario(self, dni):
        consulta = f'SELECT * FROM public."usuarios" WHERE dni_empleado = {dni};'
        return self.base.obtener_un_elemento(consulta)

    def obtener_todos_usuarios(self, opcion):
        orden = [
            "dni_empleado",
            "nombre_empleado",
            "apellido_empleado",
            "nombre_usuario",
        ]
        consulta = f'SELECT * FROM public."usuarios" ORDER BY {orden[opcion]};'
        return self.base.obtener_elementos(consulta)

    # def obtener_usuarios_filtro(self)


# print(UsuarioDAO().obtener_un_usuario("27749499"))
# print(UsuarioDAO().obtener_todos_usuarios(1))
