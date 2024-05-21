from PyQt6.QtWidgets import QApplication, QComboBox, QLabel, QTableWidget, QHBoxLayout, QVBoxLayout, QWidget, QFrame

from ventana_principal import VentanaPrincipal

class VentanaVenta(VentanaPrincipal):
    def __init__(self):
        super().__init__()

        self.BienvenidoLB.setText("VENTAS")
        self.StockBT.setText("AGREGAR")
        self.VentaBt.setText("ELIMINAR")
        self.UsuarioBt.setText("CERRAR")
        self.InformeBt.setText("LIMPIAR")
        
        self.frame_central = QFrame()
        self.frame_central.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.verticalLayout_contenido.addWidget(self.frame_central)
        
        self.horizontal_layout = QHBoxLayout(self.frame_central)
        
        # Frame para la tabla
        self.frame_tabla = QFrame()
        self.frame_tabla.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.frame_tabla.setFixedWidth(580)
        
        # Layout vertical para los botones del menú
        self.layout_tabla = QVBoxLayout(self.frame_tabla)
        
        # Creamos la tabla
        self.tabla_contenido = QTableWidget()
       # self.tabla_contenido.setFixedWidth(600)
       # self.tabla_contenido.setFixedWidth(500)
        self.tabla_contenido.setRowCount(20)
        self.tabla_contenido.setColumnCount(4)
        self.tabla_contenido.setHorizontalHeaderLabels(["Producto", "Cantidad", "Porcion/Medida", "Pensar algo + "])
        self.layout_tabla.addWidget(self.tabla_contenido)

         # Establecer el ancho de todas las columnas
        for i in range(self.tabla_contenido.columnCount()):
            self.tabla_contenido.setColumnWidth(i, 130)
        # Frame para los combo boxes
        self.frame_combo = QFrame()
        self.frame_combo.setStyleSheet("background-color: rgb(135, 206, 235);")
        
        
        # Layout vertical para los botones del menú
        self.layout_combo = QVBoxLayout(self.frame_combo)

        # Creamos unos QComboBox
        self.combo1 = QComboBox()
        self.combo1.addItems(["PRODUCTO", "Opción 2", "Opción 3"])
        self.combo1.setFixedWidth(150)

        self.combo2 = QComboBox()
        self.combo2.addItems(["CANTIDAD", "Opción B", "Opción C"])
        self.combo2.setFixedWidth(150)

        self.combo3 = QComboBox()
        self.combo3.addItems(["GR/ML", "Opción B", "Opción C"])
        self.combo3.setFixedWidth(150)

        # Creamos un QVBoxLayout para los QComboBox
      
        self.layout_combo.addWidget(self.combo1)
        self.layout_combo.addWidget(self.combo2)
        self.layout_combo.addWidget(self.combo3)

        self.horizontal_layout.addWidget(self.frame_tabla)
        self.horizontal_layout.addWidget(self.frame_combo)

if __name__ == "__main__":
    app = QApplication([])
    window = VentanaVenta()
    window.show()
    app.exec()
