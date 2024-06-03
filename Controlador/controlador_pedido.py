import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from datetime import datetime
import re
#sys.path.append('C://Users//camus//Desktop//SG_Cafeteria)//Visual')
#sys.path.append('C://Users//camus//Desktop//SG_Cafeteria//Modelo')

from Modelo.producto_DAO import ProductoDAO
from Visual.vista_pedido import VentanaPedido 
from Visual.vista_factura import PDF 




class ControladorPedido:
    def __init__(self):
        self.__vista_pedido = VentanaPedido(self)
        self.__vista_pedido.show()

       
        producto_dao = ProductoDAO()
        self.productos_bebida = producto_dao.obtener_productos_categoria("A")
        self.productos_comida = producto_dao.obtener_productos_categoria("B")
        self.productos_helado = producto_dao.obtener_productos_categoria("C")
        self.bebidas = [producto[1] for producto in self.productos_bebida]
        self.comida = [producto[1] for producto in self.productos_comida]
        self.helados = [producto[1] for producto in self.productos_helado]

        productos = producto_dao.obtener_todos_productos()
        self.precios = [producto[6] for producto in productos]
        self.diccionario_pedidos = {}
     
        # Llenar las tablas con los productos obtenidos
        self.llenar_tabla(self.__vista_pedido._tabla_comida, self.bebidas)
        self.llenar_tabla(self.__vista_pedido._tabla_bebidas, self.comida)
        self.llenar_tabla(self.__vista_pedido._tabla_helados, self.helados)
        print("Cantidad de botones en el diccionario:", len(self.__vista_pedido._botones_sumar))
        for producto in self.__vista_pedido._productos_agregados:
            print(f"Descripción: {producto[0]}, Cantidad: {producto[1]}")

             

    def llenar_tabla(self, tabla, productos):
        for producto in productos:
            self.__vista_pedido.agregarFilaConBotones(tabla, producto)  

    def llenar_tabla_pedido(self, tabla, indice_modificado, nueva_cantidad, nuevo_precio):
        producto, cantidad = self.__vista_pedido._productos_agregados[indice_modificado]
        
        # Verificar si la cantidad es mayor que cero y si el producto está en la lista
        if producto not in self.diccionario_pedidos and cantidad == 1:        
            boton = self.__vista_pedido.agregarFilaConBotonEliminar(tabla, producto, nuevo_precio)
      

            self.diccionario_pedidos[producto] = boton
            print(f'prubea del boton  {boton.itemAt(3)}')
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
                            etiqueta_canti.setText(f'{nuevo_precio:.2f}')

                    etiqueta_cantidad_item = layout.itemAt(3)  # Obtienela etiqueta de cantidad
                    if etiqueta_cantidad_item:
                        etiqueta_cantidad = etiqueta_cantidad_item.widget()  # Obtiene la etiqueta de cantidad
                        if etiqueta_cantidad:
                            print(nueva_cantidad)
                            etiqueta_cantidad.setText(str(nueva_cantidad)) 
        if producto in self.diccionario_pedidos and cantidad == 0:# Eliminar el layout del producto si la cantidad es 0
            layout = self.diccionario_pedidos.get(producto)
            for i in range(self.__vista_pedido._tabla_pedido.count()):
                layout_item = self.__vista_pedido._tabla_pedido.itemAt(i)
                if layout_item.layout() == layout:                   
                    while layout.count():
                        child = layout.takeAt(0)
                        if child.widget():
                            child.widget().deleteLater()                   
                    self.__vista_pedido._tabla_pedido.removeItem(layout_item)# Eliminar el layout del pedido
                    layout_item.deleteLater()
                    break
           
            del self.diccionario_pedidos[producto]# Eliminar la entrada del diccionario con el pedido
  

            
   

    def boton_presionado(self):
            boton_presionado = self.__vista_pedido.sender()  # Obtener el botón que generó el evento
            print("Botón seleccionado:", boton_presionado.text())          
            
            if boton_presionado in self.__vista_pedido._botones_sumar:
                print("Se presionó un botón de sumar.")
                # Obtener la ubicación del botón en la lista
                ubicacion = self.__vista_pedido._botones_sumar.index(boton_presionado)# Obtener la ubicación del botón en la lista
                print("Ubicación del botón suma:", ubicacion)
                self.sumar_etiqueta_cantidad(ubicacion)
    
            elif boton_presionado in self.__vista_pedido._botones_restar:
                print("Se presionó un botón de restar.")
                ubicacion = self.__vista_pedido._botones_restar.index(boton_presionado)
                print("Ubicación del botón resta :", ubicacion)
               
                self.restar_etiqueta_cantidad(ubicacion)
            else:
                print("Botón no identificado.")

    def sumar_etiqueta_cantidad(self, indice):
            etiqueta_cantidad = self.__vista_pedido._etiquetas_cantidad[indice]# Obtener la etiqueta de cantidad en la misma posición que el botón
            precio_producto = self.precios[indice]           
            cantidad_actual = int(etiqueta_cantidad.text())
            nueva_cantidad = cantidad_actual + 1
            nuevo_precio = precio_producto * nueva_cantidad
            etiqueta_cantidad.setText(str(nueva_cantidad))
            self.__vista_pedido._productos_agregados[indice] = (self.__vista_pedido._productos_agregados[indice][0], nueva_cantidad)
            print(self.__vista_pedido._productos_agregados[indice])
            self.llenar_tabla_pedido(self.__vista_pedido._tabla_pedido, indice, nueva_cantidad, nuevo_precio)

    def restar_etiqueta_cantidad(self, indice):
           
            etiqueta_cantidad = self.__vista_pedido._etiquetas_cantidad[indice]
            precio_producto = self.precios[indice]
            cantidad_actual = int(etiqueta_cantidad.text())
        
            if cantidad_actual > 0:
                nueva_cantidad = cantidad_actual - 1
                nuevo_precio = precio_producto * nueva_cantidad
                etiqueta_cantidad.setText(str(nueva_cantidad))
                self.__vista_pedido._productos_agregados[indice] = (self.__vista_pedido._productos_agregados[indice][0], nueva_cantidad)
                print(self.__vista_pedido._productos_agregados[indice])
                self.llenar_tabla_pedido(self.__vista_pedido._tabla_pedido, indice, nueva_cantidad, nuevo_precio)

    def cerrar_pedido(self):# para imrpimir la factura y posible actualizar base 
        lista_widgets = []

        for producto, layout in self.diccionario_pedidos.items():
            item_1 = layout.itemAt(1)
            widget_1 = item_1.widget() 
            item1 =  widget_1.text()          
        
            item_3 = layout.itemAt(3)
            widget_3 = item_3.widget() 
            item3 =  widget_3.text()  

            item_5 = layout.itemAt(5)
            widget_5 = item_5.widget() 
            item5 =  widget_5.text()  
   
            lista_widgets.append((item1, item3, float(item5)))
            
            for widgets in lista_widgets:
                    print(widgets)

        
        pdf = PDF()
        pdf.crear_factura(nro_factura = '001', fecha= datetime.now(), lista_pedido=  lista_widgets, nro_mesa= '05', metodo_pago = 'Efectivo', empleado='Juan', dni= '39910232')

"""
if __name__ == "__main__":
    app = QApplication([])
    controlador_pedido = ControladorPedido()
    app.exec()
"""
