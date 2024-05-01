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
                conn=psycopg2.connect(
                    "postgresql://neondb_owner:wiNYtFRd70MD@ep-lucky-union-a7zkmfpp.ap-southeast-2.aws.neon.tech/neondb?sslmode=require"
                )
            )
            print("Conexión exitosa")
        except Exception as ex:
            print(ex)
#------------------------------------------------------------------------------------------------------------------------------
# Crear tabla USUARIOS
self.cursor = self.conexion.cursor()

        self.crear_tablas_usuarios = """
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario SERIAL PRIMARY KEY,
                dni_empleado INT,
                nombre_empleado VARCHAR(10),
                apellido_empleado VARCHAR(10),
                cod_cargo INT,
                nombre_usuario VARCHAR(10),
                contra VARCHAR(10),
                usuario_eliminado BOOLEAN,
                causa_eliminacion VARCHAR(40)
            )
        """
        
        self.insertar_valores= """
            INSERT INTO usuarios ( dni_empleado, nombre_empleado, apellido_empleado,cod_cargo, nombre_usuario, contra, usuario_eliminado, causa_eliminacion)
            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)
        """
    def crear_tabla(self):
        self.cursor.execute(self.crear_tablas)
        self.conexion.commit()
        print("tabla creada")

    def insertar_usuarios(self, dni_empleado, nombre_empleado, apellido_empleado,cod_cargo, nombre_usuario, contra, usuario_eliminado, causa_eliminacion ):
        self.cursor.execute(self.insertar_valores, ( dni_empleado, nombre_empleado, apellido_empleado, cod_cargo,nombre_usuario, contra, usuario_eliminado, causa_eliminacion))
        self.conexion.commit()
        print("Empleado insertado correctamente.")

base_de_datos = BaseDeDatos()

# Crear la tabla 'usuarios' si no existe
base_de_datos.crear_tabla()

# Insertar  empleado
for _ in range(1):
    id_usuario_generado = random.randint(1, 999)
    dni_empleado_generado = faker.unique.random_int(25000000, 44999999)
    nombre_empleado_generado = faker.first_name()[:10]
    apellido_empleado_generado = faker.last_name()[:10]
    nombre_usuario_generado = faker.user_name()[:10]
    contra_generado = faker.password()[:10]
    usuario_eliminado_generado = False
    causa_eliminacion_generado = None
    
    base_de_datos.insertar_usuarios( dni_empleado_generado, nombre_empleado_generado, apellido_empleado_generado,5, nombre_usuario_generado, contra_generado, usuario_eliminado_generado, causa_eliminacion_generado)

base_de_datos.cursor.close()
base_de_datos.conexion.close()
#------------------------------------------------------------------------------------------------------------------------------
#Crear Tabla CARGO
       self.cursor = self.conexion.cursor()
       
        self.crear_tablas_cargos = """
            CREATE TABLE IF NOT EXISTS cargos (
                cod_cargo SERIAL PRIMARY KEY,
                descripcion VARCHAR(10)
                 
            )
        """
        
        self.insertar_valores= """
            INSERT INTO cargos (descripcion)
            VALUES ( %s )
        """
    def crear_tabla_cargos(self):
        self.cursor.execute(self.crear_tablas)
        self.conexion.commit()
        print("tabla creada")

    def insertar_cargos( self,descripcion):
        self.cursor.execute(self.insertar_valores ,( descripcion,))
        self.conexion.commit()
        print(" insertado correctamente.")

base_de_datos = BaseDeDatos()

base_de_datos.crear_tabla()

base_de_datos.insertar_cargos("Gerente")
base_de_datos.insertar_cargos("Mesero")
base_de_datos.insertar_cargos("Cajero")
base_de_datos.insertar_cargos("Barista")
base_de_datos.insertar_cargos("Cocinero")


base_de_datos.cursor.close()
base_de_datos.conexion.close()
#------------------------------------------------------------------------------------------------------------------------------
#Crear tabla FORMA_PAGO
        self.cursor = self.conexion.cursor()

        self.crear_tablas = """
            CREATE TABLE IF NOT EXISTS forma_pago (
                codigo_pago SERIAL PRIMARY KEY,
                descripcion VARCHAR(25),
                habilitado BOOLEAN,
                descuento REAL 
            )
        """
        
        self.insertar_valores= """
            INSERT INTO forma_pago ( descripcion, habilitado, descuento)
            VALUES ( %s, %s, %s)
        """
    def crear_tabla_forma_pago(self):
        self.cursor.execute(self.crear_tablas)
        self.conexion.commit
        print("tabla creada")

    def insertar_pagos(self, descripcion, habilitado, descuento):
        self.cursor.execute(self.insertar_valores, ( descripcion, habilitado, descuento))
        self.conexion.commit()
        print(" insertado correctamente.")

base_de_datos = BaseDeDatos()

base_de_datos.crear_tabla_forma_pago()

base_de_datos.insertar_pagos("Contado Efectivo", True, 20.0)
base_de_datos.insertar_pagos("Tarjeta de Credito", True, 0.0)
base_de_datos.insertar_pagos("Transferencia Bancaria", True, 10.0)

base_de_datos.cursor.close()
base_de_datos.conexion.close()
#------------------------------------------------------------------------------------------------------------------------------
#Crear tabla PRODUCTOS

        self.cursor = self.conexion.cursor()

      
        self.crear_tablas_productos= """
            CREATE TABLE IF NOT EXISTS productos (
                codigo_producto SERIAL PRIMARY KEY,
                descripcion VARCHAR(25),
                fecha DATE,
                cantidad INT,
                stock_minimo INT, 
                precio_unitario  REAL,
                vigente BOOLEAN,
                motivo_baja VARCHAR(40)

            )
        """
        
        self.insertar_valores= """
            INSERT INTO productos ( descripcion, fecha, cantidad, stock_minimo, precio_unitario, vigente, motivo_baja )
            VALUES ( %s, %s, %s, %s, %s, %s, %s )
        """
    def crear_tabla_productos(self):
        self.cursor.execute(self.crear_tablas)
        self.conexion.commit()
        print("tabla creada")

    def insertar_producto( self,descripcion, fecha, cantidad, stock_minimo, precio_unitario,vigente, motivo_baja):
        self.cursor.execute(self.insertar_valores, ( descripcion, fecha, cantidad, stock_minimo, precio_unitario,vigente, motivo_baja))
        self.conexion.commit()
        print(" insertado correctamente.")

base_de_datos = BaseDeDatos()

base_de_datos.crear_tabla()

base_de_datos.insertar_producto("Café en grano", "2024-04-30", 5, 2, 100,True, None)
base_de_datos.insertar_producto("Té negro", "2024-04-30", 200, 100, 5,True, None)
base_de_datos.insertar_producto("Leche", "2024-04-30", 150, 80, 150,True, None)
base_de_datos.insertar_producto("Azúcar", "2024-04-30", 50, 30, 30,True, None)
base_de_datos.insertar_producto("Jarabe de vainilla", "2024-04-30", 10, 5, 250,True, None)
base_de_datos.insertar_producto("Chocolate en polvo", "2024-04-30", 80, 50, 150,True, None)
base_de_datos.insertar_producto("Crema líquida", "2024-04-30", 100, 50, 250,True, None)
base_de_datos.insertar_producto("Agua mineral", "2024-04-30", 100, 40, 80,True, None)
base_de_datos.insertar_producto("Zumo de naranja", "2024-04-30", 100, 40, 100,True, None)
base_de_datos.insertar_producto("Muffin de arándanos", "2024-04-30", 100, 40, 15,True, None)
base_de_datos.insertar_producto("Alfajor de chocolate", "2024-04-30", 150, 80, 20,True, None)

base_de_datos.cursor.close()
base_de_datos.conexion.close()
#------------------------------------------------------------------------------------------------------------------------------
#Crear tabla FACTURA
     CREATE TABLE IF NOT EXISTS facturas (
                nro_factura SERIAL PRIMARY KEY,
                cod_prodcuto INT,
                cantidad INT,
                monto REAL,
                fecha_hora TIMESTAMP,
                nro_mesa INT,
                cod_pago INT,
                id_empeado INT,
                monto_total REAL
                 
            )
        """
  
    def crear_tabla(self):
        self.cursor.execute(self.crear_tablas)
        self.conexion.commit()
        print("tabla creada")

base_de_datos = BaseDeDatos()

base_de_datos.crear_tabla()
base_de_datos.cursor.close()
base_de_datos.conexion.close()
#------------------------------------------------------------------------------------------------------------------------------

    
    def obtener_un_elemento(self, consulta):
        """Devuelve un elemento de la base de datos según la consulta realizada"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta)
            return cursor.fetchone()
        except Exception as ex:

            return f"{ex} n/Error en la consulta: {consulta}. n/No se pudo obtener el elemento de la base de datos."

    def obtener_elementos(self, consulta):
        """Devuelve uno o más elementos de la base de datos según la consulta realizada"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta)
            return cursor.fetchall()
        except Exception as ex:
            return f"{ex} n/Error en la consulta: {consulta}. n/No se pudieron obtener los elemento de la base de datos."

    def consulta(self, consulta, valores):
        """Permite realizar consultas a la base de datos."""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta, valores)
            return cursor.connection.commit()
        except Exception as ex:
            return f"{ex} n/Error en la consulta: {consulta}."
