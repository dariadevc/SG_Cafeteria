import psycopg2
from abc import ABC, abstractmethod


class BaseDeDatosMeta(type):
    """Se asegura que exista solo una instancia de la base de datos"""

    __instances = None

    def __call__(cls, *args, **kwargs):
        if cls.__instances is None:
            instance = super().__call__(*args, **kwargs)
            cls.__instances = instance
        return cls.__instances


class BaseDeDatos(metaclass=BaseDeDatosMeta):
    """Maneja la conexión con la base de datos instanciada."""

    def __init__(self):
        try:
            self.conexion = psycopg2.connect(
                "postgresql://neondb_owner:wiNYtFRd70MD@ep-lucky-union-a7zkmfpp.ap-southeast-2.aws.neon.tech/neondb?sslmode=require"
            )
            print("Conexión exitosa")
        except Exception as ex:
            print(ex)

    def obtener_un_elemento(self, consulta):
        """Devuelve un elemento de la base de datos según la consulta realizada"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta)
            return cursor.fetchone()
        except Exception as ex:

            return f"{ex} Error en la consulta: {consulta}. No se pudo obtener el elemento de la base de datos."

    def obtener_elementos(self, consulta):
        """Devuelve uno o más elementos de la base de datos según la consulta realizada"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta)
            return cursor.fetchall()
        except Exception as ex:
            return f'{ex} Error en la consulta: "{consulta}". No se pudieron obtener los elemento de la base de datos.'

    def consulta(self, consulta, valores):
        """Permite realizar consultas a la base de datos."""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta, valores)
            return cursor.connection.commit()
        except Exception as ex:
            return f"{ex} Error en la consulta: {consulta}."
