import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from datetime import datetime
import re

# sys.path.append('C://Users//camus//Desktop//SG_Cafeteria)//Visual')
# sys.path.append('C://Users//camus//Desktop//SG_Cafeteria//Modelo')

from Modelo.producto_DAO import ProductoDAO
from Modelo.factura_DAO import FacturaDAO
from Visual.vista_pedido import VentanaPedido
from Visual.vista_factura import PDF


class ControladorPedido:
    def __init__(
        self,
        id_usuario,
        numero_mesa,
        actualizar_mesa_callback,
        productos_seleccionados=None,
    ):
        self.__vista_pedido = VentanaPedido(self, numero_mesa)
        self.__vista_pedido.show()
        # self.__vista_pedido.closed.connect(self.cerrar_ventana_pedido)
        self.__id_usuario = id_usuario
        self.__numero_mesa = numero_mesa
        self.__actualizar_mesa_callback = actualizar_mesa_callback
        self.__productos_seleccionados = productos_seleccionados or {}

        self.__producto_dao = ProductoDAO()
        self.__productos_bebida = self.__producto_dao.obtener_productos_categoria("A")
        self.__productos_comida = self.__producto_dao.obtener_productos_categoria("B")
        self.__productos_helado = self.__producto_dao.obtener_productos_categoria("C")
        self.__bebidas = [producto[1] for producto in self.__productos_bebida]
        self.__comida = [producto[1] for producto in self.__productos_comida]
        self.__helados = [producto[1] for producto in self.__productos_helado]

        self.productos = self.__producto_dao.obtener_todos_productos()
        self.precios = [producto[6] for producto in self.productos]
        self.stock = [producto[4] for producto in self.productos]
        self.diccionario_pedidos = {}
        self.__total= 0

        # Llenar las tablas con los productos obtenidos
        self.llenar_tabla(self.__vista_pedido.tabla_comida, self.__bebidas)
        self.llenar_tabla(self.__vista_pedido.tabla_bebidas, self.__comida)
        self.llenar_tabla(self.__vista_pedido.tabla_helados, self.__helados)
        print(
            "Cantidad de botones en el diccionario:",
            len(self.__vista_pedido.botones_sumar),
        )
        for producto in self.__vista_pedido.productos_agregados:
            print(f"Descripción: {producto[0]}, Cantidad: {producto[1]}")

        ## instancia facturaDAO
        self.__factura = FacturaDAO()

    def llenar_tabla(self, tabla, productos):
        for producto in productos:
            self.__vista_pedido.agregarFilaConBotones(tabla, producto)

    def llenar_tabla_pedido(
         self, tabla, indice_modificado, nueva_cantidad, nuevo_precio, precio_producto,es_negativo
    ):
        producto, cantidad = self.__vista_pedido.productos_agregados[indice_modificado]

        # Verificar si la cantidad es mayor que cero y si el producto está en la lista
        if producto not in self.diccionario_pedidos and cantidad == 1:
            boton = self.__vista_pedido.agregarFilaConBotonEliminar(
                tabla, producto, nuevo_precio
            )

            self.diccionario_pedidos[producto] = boton
            print(f"prubea del boton  {boton.itemAt(3)}")
        if producto in self.diccionario_pedidos and cantidad > 0:
            print("entro por el elif ")
            layout = self.diccionario_pedidos.get(producto)

            for producto, layout in self.diccionario_pedidos.items():
                print(f"Producto del diccionario : {producto}, Layout: {layout}")
            if layout:
                print("se encontro layout")

                etiqueta_precio = layout.itemAt(5)
                if etiqueta_precio:
                    etiqueta_canti = etiqueta_precio.widget()
                    if etiqueta_canti:
                        etiqueta_canti.setText(f"{nuevo_precio:.2f}")

                etiqueta_cantidad_item = layout.itemAt(
                    3
                )  # Obtienela etiqueta de cantidad
                if etiqueta_cantidad_item:
                    etiqueta_cantidad = (
                        etiqueta_cantidad_item.widget()
                    )  # Obtiene la etiqueta de cantidad
                    self.stock_producto = self.stock[indice_modificado]
                    if cantidad <= self.stock_producto:
                        print(nueva_cantidad)
                        etiqueta_cantidad.setText(str(nueva_cantidad))
                    else:
                        etiqueta_cantidad.setStyleSheet(" color: red;")
                        QTimer.singleShot(
                            2000,
                            lambda: etiqueta_cantidad.setStyleSheet("color: black;"),
                        )
        if (
            producto in self.diccionario_pedidos and cantidad == 0
        ):  # Eliminar el layout del producto si la cantidad es 0
            layout = self.diccionario_pedidos.get(producto)
            for i in range(self.__vista_pedido.tabla_pedido.count()):
                layout_item = self.__vista_pedido.tabla_pedido.itemAt(i)
                if layout_item.layout() == layout:
                    while layout.count():
                        child = layout.takeAt(0)
                        if child.widget():
                            child.widget().deleteLater()
                    self.__vista_pedido.tabla_pedido.removeItem(
                        layout_item
                    )  # Eliminar el layout del pedido
                    layout_item.deleteLater()
                    break

            del self.diccionario_pedidos[
                producto
            ]  # Eliminar la entrada del diccionario con el pedido
        if es_negativo:
            self.__total -= precio_producto
            print(f'precio restar : {self.__total}')
        else:
            self.__total += precio_producto
            print(f'precio sumar : {self.__total}')
        self.__vista_pedido.etiqueta_total.setText(f"TOTAL  :  $  {self.__total:.2f}")
    def boton_presionado(self):
        boton_presionado = (
            self.__vista_pedido.sender()
        )  # Obtener el botón que generó el evento
        print("Botón seleccionado:", boton_presionado.text())

        if boton_presionado in self.__vista_pedido.botones_sumar:
            print("Se presionó un botón de sumar.")
            # Obtener la ubicación del botón en la lista
            ubicacion = self.__vista_pedido.botones_sumar.index(
                boton_presionado
            )  # Obtener la ubicación del botón en la lista
            print("Ubicación del botón suma:", ubicacion)
            self.sumar_etiqueta_cantidad(ubicacion)

        elif boton_presionado in self.__vista_pedido.botones_restar:
            print("Se presionó un botón de restar.")
            ubicacion = self.__vista_pedido.botones_restar.index(boton_presionado)
            print("Ubicación del botón resta :", ubicacion)

            self.restar_etiqueta_cantidad(ubicacion)
        else:
            print("Botón no identificado.")

    def sumar_etiqueta_cantidad(self, indice):
        etiqueta_cantidad = self.__vista_pedido.etiquetas_cantidad[
            indice
        ]  # Obtener la etiqueta de cantidad en la misma posición que el botón
        precio_producto = self.precios[indice]
        cantidad_actual = int(etiqueta_cantidad.text())
        nueva_cantidad = cantidad_actual + 1
        nuevo_precio = precio_producto * nueva_cantidad
        etiqueta_cantidad.setText(str(nueva_cantidad))
        self.__vista_pedido.productos_agregados[indice] = (
            self.__vista_pedido.productos_agregados[indice][0],
            nueva_cantidad,
        )
        print(self.__vista_pedido.productos_agregados[indice])
        self.llenar_tabla_pedido(
            self.__vista_pedido.tabla_pedido, indice, nueva_cantidad, nuevo_precio, precio_producto,es_negativo = False
                          )

    def restar_etiqueta_cantidad(self, indice):

        etiqueta_cantidad = self.__vista_pedido.etiquetas_cantidad[indice]
        precio_producto = self.precios[indice]
        cantidad_actual = int(etiqueta_cantidad.text())

        if cantidad_actual > 0:
            nueva_cantidad = cantidad_actual - 1
            nuevo_precio = precio_producto * nueva_cantidad
            etiqueta_cantidad.setText(str(nueva_cantidad))
            self.__vista_pedido.productos_agregados[indice] = (
                self.__vista_pedido.productos_agregados[indice][0],
                nueva_cantidad,
            )
            print(self.__vista_pedido.productos_agregados[indice])
            self.llenar_tabla_pedido(
                self.__vista_pedido.tabla_pedido, indice, nueva_cantidad, nuevo_precio, precio_producto,es_negativo = True
            )

    def finalizar_pedido(self):  # para imrpimir la factura y posible actualizar base
        lista_widgets = []
        lista_widget_stock = []

        for producto, layout in self.diccionario_pedidos.items():
            item_1 = layout.itemAt(1)
            widget_1 = item_1.widget()
            item1 = widget_1.text()

            item_3 = layout.itemAt(3)
            widget_3 = item_3.widget()
            item3 = widget_3.text()

            item_5 = layout.itemAt(5)
            widget_5 = item_5.widget()
            item5 = widget_5.text()

            lista_widgets.append((item1, item3, float(item5)))
            lista_widget_stock.append((item1, item3))

        for nombre, cantidad in lista_widget_stock:
            for producto in self.productos:
                if nombre == producto[1]:
                    codigo = producto[0]
                    break
            print(codigo)
            print(cantidad)
            self.__producto_dao.disminuir_stock(codigo, cantidad)

        # Agregar la factura a la base de datos
        monto_bruto = sum(float(item[2]) for item in lista_widgets)
        nro_factura = self.formatear_numero_factura(self.__numero_mesa)
        id_factura = self.__factura.agregar_factura(
            monto_bruto=monto_bruto,
            nro_mesa=self.__numero_mesa,
            cod_pago=1,  # Acá deberíamos agregar el código del pago
            id_empleado=self.__id_usuario,  # Acá deberíamos agregar el id del usuario que esta usando el sistema
            monto_total=monto_bruto,  # Acá debería aplicarse el descuento si lo hacemos
        )

        # Agregar los detalles de la factura a la base de datos
        for producto, cantidad, precio in lista_widgets:
            for prod in self.productos:
                if prod[1] == producto:
                    id_producto = prod[0]
                    break
            self.__factura.agregar_detalle_factura(id_factura, id_producto, cantidad)

        pdf = PDF()
        pdf.crear_factura(
            nro_factura=self.formatear_numero_factura(id_factura),
            fecha=datetime.now(),
            lista_pedido=lista_widgets,
            nro_mesa=self.__numero_mesa,
            metodo_pago="Efectivo",
            empleado=self.__id_usuario,
            dni="39910232",
        )
        self.__actualizar_mesa_callback(self.__numero_mesa, "libre")
        self.__vista_pedido.close()

        # Elimina instancia de pedido del diccionario de pedido
        # del self.controladores_pedidos[self.numero_mesa]

    def formatear_numero_factura(self, nro_factura, longitud=7):
        return "0000-" + str(nro_factura).zfill(longitud)

    def anular_pedido(self):
        self.__actualizar_mesa_callback(self.__numero_mesa, "libre")
        self.__vista_pedido.close()
        # del self.controladores_pedidos[self.numero_mesa]

    def cerrar_ventana_pedido(self):
        print(f"Ventana del pedido de la mesa {self.__numero_mesa} cerrada")

    def abrir_ventana_pedido(self):
        self.__vista_pedido.show()
