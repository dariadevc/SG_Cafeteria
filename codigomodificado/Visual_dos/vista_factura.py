import sys, os, subprocess
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtWidgets import QApplication
from fpdf import FPDF

class PDF(FPDF):

    def crear_factura(self,nro_factura, fecha, lista_pedido,nro_mesa, metodo_pago, empleado, dni):
        self.__nro_factura = nro_factura
        self.__fecha = fecha
        self.__lista_pedido = lista_pedido
        self.__nro_mesa = nro_mesa    
        self.__metodo_pago = metodo_pago
        self.__empleado = empleado
        self.__dni = dni
        
        app = QApplication([])  

        canti_filas = len(self.__lista_pedido)

        pdf = PDF(format=(100.732, 350.973))
        pdf.add_page()
        pdf.set_font('Arial', 'B', 12)    
        pdf.cell(0, 10, 'CAFETERIA VIERA', 0, 1, 'C')
        pdf.set_font('Arial', '', 12)
        #C:/Users/Alambrito/Documents/GitHub/
#        pdf.image("C://Users//camus//Desktop//SG_Cafeteria_clone//Visual//imagenes//coffe.png", x=0, y=25, w=30,h=25)
        pdf.image("C://Users//Alambrito//Documents//Github//SG_Cafeteria//Visual//imagenes//coffe.png", x=0, y=25, w=30,h=25)
        pdf.cell(200, 10, txt = "                        C.U.I.T : 20-13243654-39 ", ln = True, align = 'L')
        pdf.cell(200, 10, txt = "                        INGR. BRUTOS : 244541-02 ", ln = True, align = 'L')
        pdf.cell(200, 10, txt = "                        AV. SAN MARTIN 534", ln = True, align = 'L')
        pdf.cell(200, 10, txt = "                        COM. RIVADAVIA., CP 9000", ln = True, align = 'L')
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(200, 10, txt = "-----------------------------------------------------", ln = True, align = 'L')
        pdf.set_font('Arial', '', 12)
        pdf.cell(200, 5, txt = f"Nro. de factura : {self.__nro_factura}", ln = True, align = 'L')
        pdf.cell(200, 5, txt = f"Fecha : {self.__fecha}", ln = True, align = 'L')
        pdf.cell(200, 5, txt = f"Nro. de mesa : {self.__nro_mesa}", ln = True, align = 'L')
        pdf.cell(200, 5, txt = "Codigo  Cant.  Precio Uni.  Precio tot.", ln = True, align = 'L')
        
        self.__total = 0
        self.__descuento = 0
        for i in range(0, canti_filas):
            self.__cod_producto, self.__cantidad, self.__precio_unitario = self.__lista_pedido[i]
            self.__parcial_total = int(self.__precio_unitario) * int(self.__cantidad)
            self.__total += self.__parcial_total
            pdf.cell(0, 10, '{:<6}    {:<6}    {:<6.2f}         {:>6.2f}'.format(self.__cod_producto, self.__cantidad, self.__precio_unitario, self.__parcial_total), 0, 1)

           
        pdf.cell(200, 5, txt = f"Subtotal $ {self.__total:.2f}          Descuento $ {self.__descuento:.2f} ", ln = True, align = 'L')
        pdf.cell(200, 5, txt = f"Total $ {self.__total:.2f}", ln = True, align = 'L')
        pdf.cell(200, 5, txt = f"Metodo de pago : {self.__metodo_pago}", ln = True, align = 'L')
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(200, 10, txt = "----------------------------------------------------", ln = True, align = 'L')
        pdf.set_font('Arial', '', 12)
        pdf.cell(200, 10, txt = f"Empleado : {self.__empleado}", ln = True, align = 'L')
        pdf.cell(200, 10, txt = f"DNI : {self.__dni}", ln = True, align = 'L')

        # Imprime el PDF
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        output_file = 'output.pdf'
        printer.setOutputFileName(output_file)
        pdf.output(output_file)

        # Abre el PDF automáticamente
        output_file = output_file
        subprocess.Popen(['start', output_file], shell=True)

      
        app.quit()
