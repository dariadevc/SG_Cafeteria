from Visual_dos.vista_vendedor import VistaVendedor
from Visual_dos.vista_venta import VentanaVenta
from Visual_dos.vista_stock import VistaStock
from Controlador_dos.controlador_venta import ControladorVenta
import Controlador_dos.controlador_inicio


class ControladorVendedor:

    def __init__(self, usuario, id_usuario):
        self.__vista_vendedor = VistaVendedor(self)
        self.__usuario = usuario
        self.__id_usuario = id_usuario
        nombre_usuario = usuario.get_usuario()
        self.__vista_vendedor.label.setText(nombre_usuario)

        ## Instancia secciones con sus controladores
        self.__controlador_venta = ControladorVenta(usuario, self.__id_usuario)
        # self.__controlador_stock = ControladorStock()
        # self.__controlador_informe = ControladorInforme()

        self.__vista_venta = self.__controlador_venta.get_vista()
        # self.__vista_stock = self.__controlador_stock.get_vista()
        self.__vista_stock = VistaStock()  # Para probar que funciona el stacked
        # self.__vista_informe = self.__controlador_informe.get_vista()

        ## Agrega secciones al stacked layout
        self.__vista_vendedor.agregar_seccion(self.__vista_venta)
        self.__vista_vendedor.agregar_seccion(self.__vista_stock)
        # self.__vista_vendedor.agregar_seccion(self.__vista_informe)

        ## Conecta los botones con los métodos para cambiar de vista
        self.__vista_vendedor.boton_venta.clicked.connect(self.cambio_a_venta)
        self.__vista_vendedor.boton_stock.clicked.connect(self.cambio_a_stock)
        self.__vista_vendedor.boton_informe.clicked.connect(self.cambio_a_informe)

        ## Conecta botón con logout
        self.__vista_vendedor.boton_cerrar.clicked.connect(self.logout)

        ## Inicia con vista venta
        self.cambio_a_venta()
        self.__vista_vendedor.show()

    def cambio_a_venta(self):
        self.__vista_vendedor.cambiar_vista(0)
        self.__vista_vendedor.actualizar_color_boton(self.__vista_vendedor.boton_venta)
        print("venta click")

    def cambio_a_stock(self):
        self.__vista_vendedor.cambiar_vista(1)
        self.__vista_vendedor.actualizar_color_boton(self.__vista_vendedor.boton_stock)
        print("stock click")

    def cambio_a_informe(self):
        # self.__vista_vendedor.cambiar_vista(2)
        self.__vista_vendedor.actualizar_color_boton(
            self.__vista_vendedor.boton_informe
        )
        print("informe click")

    def logout(self):
        self.__vista_inicio = (
            Controlador_dos.controlador_inicio.ControladorInicioSesion()
        )
        self.__vista_vendedor.close()
