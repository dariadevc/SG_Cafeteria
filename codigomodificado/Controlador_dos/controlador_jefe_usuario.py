from Visual_dos.ventana_usuario_jefe import VentanaUsuarioJefe
#from Modelo_dos.usuario import Usuario
from Modelo_dos.usuario_DAO import UsuarioDAO
import Controlador_dos.controlador_inicio
from Controlador_dos.controlador_agregar_usuarios import ControladorAgregarUsuario
from Controlador_dos.controlador_eliminar_usuarios import ControladorEliminarUsuario
from PyQt6.QtWidgets import *

class ControladorJefeUsuario:
    
    def __init__(self, usuario):
        self.__ventana_usuario_jefe = VentanaUsuarioJefe(self)
        self.__ventana_usuario_jefe.label.setText(f"Bienvenido Jefe {usuario.get_usuario()}")
        self.__ventana_usuario_jefe.show()
        self.__usuario_dao = UsuarioDAO()
        self.cargar_usuarios()
    
    def cargar_usuarios (self):
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
            
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila,0,dni)
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila,1,nombre)
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila,2,apellido)
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila,3,tipo)
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila,4,baja)
            self.__ventana_usuario_jefe.tabla_usuarios.setItem(fila,5,causa)
    
    def cerrar_sesion (self):
        self.__cerrar = Controlador_dos.controlador_inicio.ControladorInicioSesion()
        self.__ventana_usuario_jefe.close()
    
    def cambio_a_usuario (self):
        pass
    
    def cambio_a_informe (self):
        print("cambiar a informe")
    
    def cambio_a_venta (self):
        print("cambiar a venta")
    
    def cambio_a_stock (self):
        print("cambiar a stock")
    
    def agregar_usuario (self):
        self.__controlador_agregar = ControladorAgregarUsuario()
    
    def modificar_usuario (self):
        print("modificar")
        usuario_seleccionado = self.__ventana_usuario_jefe.tabla_usuarios.selectedItems()
        #self.__controlador_modificar = ControladorModificarUsuario(usuario_seleccionado)
    
    def eliminar_usuario (self):
        usuario_seleccionado = self.__ventana_usuario_jefe.tabla_usuarios.selectedItems()
        #print(usuario_seleccionado[0].text())
        self.__controlador_eliminar = ControladorEliminarUsuario(usuario_seleccionado[0].text())