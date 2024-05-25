from Visual.vista_ticket import VistaTicket

class ControladorTicket:
    def __init__(self, vista):
        self.__vista_ticket = VistaTicket()
        self.__producto_dao = ProductoDAO()
        self.__vista_ticket.btn_suma.clicked.connect(self.sumar_producto)

    def sumar_producto(self):
        items_seleccionados = self.__vista_ticket.tabla1.selectedItems()
        if len(items_seleccionados) > 0:
            fila_seleccionada = items_seleccionados[0].row()
            producto = items_seleccionados[0].text()
            cantidad_disponible = int(self.__vista_ticket.tabla1.item(fila_seleccionada, 2).text())

            if cantidad_disponible > 0: # Verifica que hayan productos disponibles
                for fila in range(self.__vista_ticket.tabla2.rowCount()):
                    if self.__vista_ticket.tabla2.item(fila, 0).text() == producto: # Verifica si el producto ya esta en la tabla2
                        cantidad_actual = int(self.__vista_ticket.tabla2.item(fila, 1).text())
                        self.__vista_ticket.tabla2.setItem(fila, 1, QTableWidgetItem(str(cantidad_actual + 1)))
                        self.__vista_ticket.tabla1.setItem(fila_seleccionada, 2, QTableWidgetItem(str(cantidad_disponible - 1)))
                        return
                fila = self.__vista_ticket.tabla2.rowCount() # Si el producto no esta en tabla2 agrega una nueva fla
                self.__vista_ticket.tabla2.insertRow(fila)
                self.__vista_ticket.tabla2.setItem(fila, 0, QTableWidgetItem(producto))
                self.__vista_ticket.tabla2.setItem(fila, 1, QTableWidgetItem("1"))  # La cantidad comienza en 1
                self.__vista_ticket.tabla1.setItem(fila_seleccionada, 2, QTableWidgetItem(str(cantidad_disponible - 1)))
        
    def restar_producto(self):
        print("se resto un producto")
        items_seleccionados = self.__vista_ticket.tabla1.selectedItems()
        if len(items_seleccionados) > 0:
            # fila_seleccionada = items_seleccionados[0].row()
            producto = items_seleccionados[0].text()

            for fila in range(self.__vista_ticket.tabla2.rowCount()):
                if self.__vista_ticket.tabla2.item(fila, 0).text() == producto:
                    cantidad_actual = int(self.__vista_ticket.tabla2.item(fila, 1).text())
                    if cantidad_actual > 1:
                        self.__vista_ticket.tabla2.setItem(fila, 1, QTableWidgetItem(str(cantidad_actual - 1)))
                    else:
                        self.__vista_ticket.tabla2.removeRow(fila)

                    for fila1 in range(self.__vista_ticket.tabla1.rowCount()):
                        if self.__vista_ticket.tabla1.item(fila1, 0).text() == producto:
                            cantidad_disponible = int(self.__vista_ticket.tabla1.item(fila1, 2).text())
                            self.__vista_ticket.tabla1.setItem(fila1, 2, QTableWidgetItem(str(cantidad_disponible + 1)))
                            return
                        

    def imprimir_producto(self):
        pdf = PDF()
        lista = [("cola cola", 2,15.65 ),("cafe doble", 2,30.65 )]
        pdf.crear_factura(nro_factura = '001', fecha= datetime.now(), lista_pedido=  lista, nro_mesa= '05', metodo_pago = 'Efectivo', empleado='Juan', dni= '39910232')