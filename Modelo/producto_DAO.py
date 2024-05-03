from base_de_datos import BaseDeDatos
from datetime import datetime


class ProductoDAO:
    def __init__(self):
        self.__base = BaseDeDatos()
        self.__fecha_actual = datetime.today().strftime("%Y-%m-%d")

    ## TODO: Consultar el tema de agregar un código extra para cada producto, con el que lo identifiquen los empleados, no en la base
    def agregar_producto(self, descripcion, fecha_modif, cantidad, minimo, precio):
        consulta = 'INSERT into public."productos"(descripcion, fecha, cantidad, stock_minimo, precio_unitario) VALUES (%s, %s, %s, %s, %s)'
        valores = (descripcion, fecha_modif, cantidad, minimo, precio)
        self.__base.consulta(consulta, valores)
        print("Se agrego a la base de datos un nuevo producto")

    ## TODO: Agregar código para identificar el producto que se va a eliminar
    def eliminar_producto(self, cod_producto, causa):
        consulta = 'UPDATE public."productos" SET vigente = %s, motivo_baja = %s WHERE {código_producto} = %s;'
        valores = (True, causa, cod_producto)
        self.__base.consulta(consulta, valores)
        print(f"Se dio la baja lógica del producto con el código {cod_producto}")

    ## TODO: Agregar los "producto_modificado.get_[x]" cuando los defina.
    def modificar_producto(self, cod_producto):  # , producto_modificado=Producto):
        consulta = 'UPDATE public."productos" SET {cod_producto} = %s, descripcion = %s, fecha = %s, cantidad = %s, stock_minimo = %s, precio_minimo = %s WHERE dni_empleado = %s;'
        valores = ()
        self.__base.consulta(consulta, valores)
        print(f"Se modificaron los datos del producto con el código {cod_producto}")

    # def obtener_un_producto(self, cod_prod):
    #     consulta = f'SELECT * FROM public."productos" WHERE {acá va cod_producto} = {cod_producto}'
    #     return self.base.obtener_un_elemento(consulta)

    def obtener_todos_productos(self, opcion):
        orden = [
            "cod_producto",
            "descripcion",
            "fecha",
            "cantidad",
            "stock_minimo",
            "precio_unitario",
        ]
        consulta = f'SELECT * FROM public."productos" ORDER BY {orden[opcion]};'
        return self.__base.obtener_elementos(consulta)

    def agregar_stock(self, cod_producto, cantidad):
        consulta = 'UPDATE public."productos" SET cantidad = cantidad + %s, fecha = %s WHERE codigo_producto = %s;'
        valores = (cantidad, self.__fecha_actual, cod_producto)
        self.__base.consulta(consulta, valores)
        print(
            f"Stock del producto {cod_producto} agregado exitosamente, cantidad = {cantidad}."
        )

    def disminuir_stock(self, cod_producto, cantidad):
        consulta = 'UPDATE public."productos" SET cantidad = cantidad - %s, fecha = %s WHERE codigo_producto = %s;'
        valores = (cantidad, self.__fecha_actual, cod_producto)
        self.__base.consulta(consulta, valores)
        print(
            f"Stock del producto {cod_producto} disminuido exitosamente, cantidad = -{cantidad}."
        )

    def obtener_stock_minimo(self, cod_producto):
        consulta = f'SELECT stock_minimo FROM public."productos" WHERE codigo_producto = {cod_producto};'
        return self.__base.obtener_un_elemento(consulta)[
            0
        ]  ## Lo devuelve como tupla aunque sea un solo elemento, con el [0] devuelve solo el número


# print(ProductoDAO().obtener_todos_productos(4))
# ProductoDAO().agregar_stock(4, 10)
# ProductoDAO().disminuir_stock(2, 10)
# print(ProductoDAO().obtener_stock_minimo(1))
