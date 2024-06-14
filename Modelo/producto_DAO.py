import logging
from Modelo.base_de_datos import BaseDeDatos
from datetime import datetime


class ProductoDAO:
    def __init__(self):
        self.__base = BaseDeDatos()
        self.__fecha_actual = datetime.today().strftime("%Y-%m-%d")

    def agregar_producto(self, descripcion, categoria, cantidad, minimo, precio):
        consulta = 'INSERT into public."productos"(descripcion, categoria, fecha, cantidad, stock_minimo, precio_unitario, vigente) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        # valores = (descripcion, fecha_modif, cantidad, minimo, precio)
        valores = (
            descripcion,
            categoria,
            self.__fecha_actual,
            cantidad,
            minimo,
            float(precio),
            True,
        )

        # Validación de entrada
        if not all([descripcion, categoria, cantidad, minimo, precio]):
            print(
                "Error: Todos los campos deben ser proporcionados y no pueden ser vacíos."
            )
            return None

        # Información de depuración
        print(f"Ejecutando consulta: {consulta}")
        print(f"Con valores: {valores}")

        try:
            self.__base.consulta(consulta, valores)
            print("Se agregó a la base de datos un nuevo producto")
        except Exception as e:
            print("Error al agregar producto a la base de datos:", e)
            # Registro del error detallado
            logging.error("Error al agregar producto a la base de datos: %s", e)
            return None

    def eliminar_producto(self, cod_producto, causa):
        consulta = 'UPDATE public."productos" SET vigente = %s, motivo_baja = %s WHERE codigo_producto = %s;'
        valores = (False, causa, cod_producto)
        try:
            self.__base.consulta(consulta, valores)
            print(f"Se dio la baja lógica del producto con el código {cod_producto}")
        except Exception as e:
            print("Error al dar la baja lógica:", e)
            return None

    ## TODO: Agregar los "producto_modificado.get_[x]" cuando los defina.
    def modificar_producto(
        self, cod_prod, categoria, descripcion, cantidad, stock, precio
    ):
        consulta = 'UPDATE public."productos" SET descripcion = %s, categoria = %s, fecha = %s, cantidad = %s, stock_minimo = %s, precio_unitario = %s WHERE codigo_producto = %s;'
        valores = (
            descripcion,
            categoria,
            self.__fecha_actual,
            cantidad,
            stock,
            precio,
            cod_prod,
        )
        self.__base.consulta(consulta, valores)
        print(f"Se modificaron los datos del producto con el código {cod_prod}")

    def obtener_un_producto(self, codigo):
        consulta = f'SELECT * FROM public."productos" WHERE codigo_producto ={codigo}'
        return self.__base.obtener_un_elemento(consulta)

    def obtener_todos_productos(self):
        consulta = 'SELECT * FROM public."productos"'
        return self.__base.obtener_elementos(consulta)

    def obtener_productos_categoria(self, categoria):
        orden = [
            "cod_producto",
            "descripcion",
            "categoria",
            "fecha",
            "cantidad",
            "stock_minimo",
            "precio_unitario",
        ]
        consulta = 'SELECT * FROM public."productos" WHERE categoria = %s;'
        valor = (categoria,)
        print("descarga los elementos por categoria")
        return self.__base.obtener_elementos(consulta, valor)

    def agregar_stock(self, cod_producto, cantidad):
        consulta = 'UPDATE public."productos" SET cantidad = cantidad + %s, fecha = %s WHERE codigo_producto = %s;'
        valores = (cantidad, self.__fecha_actual, cod_producto)
        try:
            self.__base.consulta(consulta, valores)
            print(
                f"Stock del producto {cod_producto} agregado exitosamente, cantidad agregada = {cantidad}."
            )
        except Exception as e:
            print("Error al agregar stock:", e)
            return None

    def disminuir_stock(self, cod_producto, cantidad):
        consulta = 'UPDATE public."productos" SET cantidad = cantidad - %s, fecha = %s WHERE codigo_producto = %s;'
        valores = (cantidad, self.__fecha_actual, cod_producto)

        try:
            self.__base.consulta(consulta, valores)
            print(
                f"Stock del producto {cod_producto} disminuido exitosamente, cantidad = -{cantidad}."
            )
        except Exception as e:
            print("Error al disminuir stock:", e)
            return None

    def obtener_stock_minimo(self, cod_producto):
        consulta = f'SELECT stock_minimo FROM public."productos" WHERE codigo_producto = {cod_producto};'
        return self.__base.obtener_un_elemento(consulta)[
            0
        ]  ## Lo devuelve como tupla aunque sea un solo elemento, con el [0] devuelve solo el número


# print(ProductoDAO().obtener_todos_productos(4))
# ProductoDAO().agregar_stock(4, 10)
# ProductoDAO().disminuir_stock(2, 10)
# print(ProductoDAO().obtener_stock_minimo(1))

# print(ProductoDAO().obtener_productos_categoria("A"))
