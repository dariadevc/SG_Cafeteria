import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Modelo_dos.base_de_datos import BaseDeDatos
from datetime import datetime


class FacturaDAO:
    def __init__(self):
        self.__base = BaseDeDatos()
        self.__fecha_actual = datetime.today().strftime("%Y-%m-%d")
        self.__hora_actual = datetime.today().strftime("%H:%M:%S")

    def agregar_factura(
        self,
        monto_bruto=float,
        nro_mesa=int,
        cod_pago=int,
        id_empleado=int,
        monto_total=float,
    ):
        consulta = 'INSERT into public."facturas"(monto, fecha, nro_mesa, cod_pago, id_empleado, monto_total, hora) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING nro_factura'
        valores = (
            monto_bruto,
            self.__fecha_actual,
            nro_mesa,
            cod_pago,
            id_empleado,
            monto_total,
            self.__hora_actual,
        )
        # self.__base.consulta(consulta, valores)
        ## RETURNING hace que devuelva el id de la factura recién creada
        try:
            id_factura = self.__base.obtener_un_elemento(consulta, valores)
            print("Se agrego a la base de datos una nueva factura")
            return id_factura[0]
        except Exception as e:
            print("Error al obtener las facturas por fecha:", e)
            return None

        return id_factura

    def agregar_detalle_factura(self, id_factura, id_producto, cantidad):
        consulta = 'INSERT into public."detalle_factura"(id_factura, id_producto, cantidad) VALUES (%s, %s, %s)'
        valores = (id_factura, id_producto, cantidad)
        self.__base.consulta(consulta, valores)

    # def obtener_un_producto(self, cod_prod):
    #     consulta = f'SELECT * FROM public."productos" WHERE {acá va cod_producto} = {cod_producto}'
    #     return self.base.obtener_un_elemento(consulta)

    def obtener_facturas_por_fecha(self, fecha):
        consulta = 'SELECT * FROM public."facturas" WHERE fecha = %s'
        valores = (fecha,)

        try:
            facturas = self.__base.obtener_elementos(consulta, valores)
            print(f"Se obtuvieron {len(facturas)} facturas para la fecha {fecha}")
            return facturas  # Devuelve lista con las facturas que tienen esa fecha
        except Exception as e:
            print("Error al obtener las facturas por fecha:", e)
            return None

    def obtener_producto_por_factura(self, id_factura):
        consulta = 'SELECT df.id_producto, p.descripcion, df.cantidad, p.precio_unitario FROM public."detalle_factura" df JOIN public."productos" p ON df.id_producto = p.codigo_producto WHERE df.id_factura = %s '
        valores = (id_factura,)

        try:
            detalle = self.__base.obtener_elementos(consulta, valores)
            print(
                f"Se obtuvieron {len(detalle)} productos para la factura {id_factura}"
            )
            return detalle
        except Exception as e:
            print("Error al obtener el detalle de la factura:", e)
            return None


print(FacturaDAO().obtener_producto_por_factura(1))
