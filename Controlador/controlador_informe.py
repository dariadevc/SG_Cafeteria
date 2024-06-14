import pandas as pd
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from Modelo.producto_DAO import ProductoDAO
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Visual.ventana_informe import VentanaInforme


class GenerarInforme:
    def __init__(self):
        self.__vista_informe = VentanaInforme(self)
        self.__vista_informe.show()
        self.producto = ProductoDAO()
        self.__productos_bebida = self.producto.obtener_productos_categoria("A")
        self.__productos_comida = self.producto.obtener_productos_categoria("B")
        self.__productos_helado = self.producto.obtener_productos_categoria("C")

        self.lista_comida = self.llenar_listas(self.__productos_comida)
        self.lista_bebida = self.llenar_listas(self.__productos_bebida)
        self.lista_helado = self.llenar_listas(self.__productos_helado)

        self.grafico_comida = pd.DataFrame(self.lista_comida)
        self.grafico_bebidas = pd.DataFrame(self.lista_bebida)
        self.grafico_helados = pd.DataFrame(self.lista_helado)

        canvas_comida = self.crear_grafico(self.grafico_comida, "Stock comida")
        canvas_bebida = self.crear_grafico(self.grafico_bebidas, "Stock bebida")
        canvas_helado = self.crear_grafico(self.grafico_helados, "Stock helados")

        # Ajustar la altura del canvas a 400px
        canvas_comida.setMinimumHeight(400)
        canvas_bebida.setMinimumHeight(400)
        canvas_helado.setMinimumHeight(400)

        # Agregar los canvas al layout de gráficos
        self.__vista_informe.layout_graficos.addWidget(canvas_comida)
        self.__vista_informe.layout_graficos.addWidget(canvas_bebida)
        self.__vista_informe.layout_graficos.addWidget(canvas_helado)

    def get_vista(self):
        return self.__vista_informe

    def llenar_listas(self, lista_producto):
        lista = []
        for producto in lista_producto:
            if producto[6]:
                descripcion = producto[1]
                cantidad_actual = producto[4]
                stock_minimo = producto[5]
                lista.append(
                    {
                        "Descripcion": descripcion,
                        "Cantidad actual": cantidad_actual,
                        "Stock minimo": stock_minimo,
                    }
                )
        return lista

    def crear_grafico(self, df: pd.DataFrame, titulo=str):
        fig, ax = plt.subplots(figsize=(9, 3))
        bar_width = 0.3
        posiciones = range(len(df))

        barras_stock = ax.bar(
            posiciones, df["Stock minimo"], bar_width, color="firebrick", alpha=0.7
        )
        barras_cantidad = ax.bar(
            posiciones,
            df["Cantidad actual"],
            bar_width,
            bottom=df["Stock minimo"],
            color="steelblue",
        )

        ax.set_ylabel("Cantidad")
        ax.set_title(titulo)
        ax.set_xticks(posiciones)
        ax.set_xticklabels(df["Descripcion"])
        ax.legend()
        plt.subplots_adjust(right=0.9)

        for i, barra in enumerate(barras_stock):
            altura = barra.get_height()
            ax.text(
                barra.get_x() + barra.get_width() / 2.0,
                altura,
                f"{int(altura)}",
                ha="center",
                va="bottom",
                color="black",
            )

        for i in range(len(df)):
            total = df["Stock minimo"][i] + df["Cantidad actual"][i]
            ax.text(i, total, f"{total}", ha="center", va="bottom", color="black")

        plt.xticks(rotation=45)
        plt.tight_layout()
        return FigureCanvas(fig)


# class GenerarInforme:
#     def __init__(self):
#         self.__vista_informe = VentanaInforme(self)
#         self.__vista_informe.show()
#         self.producto = ProductoDAO()
#         self.__productos_bebida = self.producto.obtener_productos_categoria("A")
#         self.__productos_comida = self.producto.obtener_productos_categoria("B")
#         self.__productos_helado = self.producto.obtener_productos_categoria("C")

#         self.lista_comida = self.llenar_listas(self.__productos_comida)
#         self.lista_bebida = self.llenar_listas(self.__productos_bebida)
#         self.lista_helado = self.llenar_listas(self.__productos_helado)

#         self.grafico_comida = pd.DataFrame(self.lista_comida)
#         self.grafico_bebidas = pd.DataFrame(self.lista_bebida)
#         self.grafico_helados = pd.DataFrame(self.lista_helado)

#         canvas_comida = self.crear_grafico(self.grafico_comida, "Stock comida")
#         canvas_bebida = self.crear_grafico(self.grafico_bebidas, "Stock bebida")
#         canvas_helado = self.crear_grafico(self.grafico_helados, "Stock helados")

#         self.__vista_informe.tabla_informe.setRowCount(3)
#         self.__vista_informe.tabla_informe.setRowHeight(0, 300)
#         self.__vista_informe.tabla_informe.setRowHeight(1, 300)
#         self.__vista_informe.tabla_informe.setRowHeight(2, 300)
#         self.__vista_informe.tabla_informe.setColumnWidth(0, 650)
#         self.__vista_informe.tabla_informe.setColumnWidth(1, 650)
#         self.__vista_informe.tabla_informe.setColumnWidth(2, 650)

#         self.__vista_informe.tabla_informe.setCellWidget(0, 0, canvas_comida)
#         self.__vista_informe.tabla_informe.setCellWidget(1, 0, canvas_bebida)
#         self.__vista_informe.tabla_informe.setCellWidget(2, 0, canvas_helado)

#     def get_vista(self):
#         return self.__vista_informe

#     def llenar_listas(self, lista_producto):
#         lista = []
#         for producto in lista_producto:
#             if producto[6]:
#                 descripcion = producto[1]
#                 cantidad_actual = producto[4]
#                 stock_minimo = producto[5]
#                 lista.append(
#                     {
#                         "Descripcion": descripcion,
#                         "Cantidad actual": cantidad_actual,
#                         "Stock minimo": stock_minimo,
#                     }
#                 )
#         return lista

#     def crear_grafico(self, df: pd.DataFrame, titulo=str):
#         fig, ax = plt.subplots(figsize=(9, 3))
#         bar_width = 0.3
#         posiciones = range(len(df))

#         barras_stock = ax.bar(
#             posiciones, df["Stock minimo"], bar_width, color="firebrick", alpha=0.7
#         )
#         barras_cantidad = ax.bar(
#             posiciones,
#             df["Cantidad actual"],
#             bar_width,
#             bottom=df["Stock minimo"],
#             color="steelblue",
#         )

#         ax.set_ylabel("Cantidad")
#         ax.set_title(titulo)
#         ax.set_xticks(posiciones)
#         ax.set_xticklabels(df["Descripcion"])
#         ax.legend()
#         plt.subplots_adjust(right=0.9)

#         for i, barra in enumerate(barras_stock):
#             altura = barra.get_height()
#             ax.text(
#                 barra.get_x() + barra.get_width() / 2.0,
#                 altura,
#                 f"{int(altura)}",
#                 ha="center",
#                 va="bottom",
#                 color="black",
#             )

#         for i in range(len(df)):
#             total = df["Stock minimo"][i] + df["Cantidad actual"][i]
#             ax.text(i, total, f"{total}", ha="center", va="bottom", color="black")

#         plt.xticks(rotation=45)
#         plt.tight_layout()
#         return FigureCanvas(fig)
