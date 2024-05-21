from PyQt6.QtWidgets import QApplication, QComboBox, QLabel, QTableWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy,QWidget, QFrame,QSizePolicy,QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt



from ventana_principal import VentanaPrincipal

class VentanaVenta(VentanaPrincipal):
    def __init__(self):
        super().__init__()

        self.BienvenidoLB.setText("USUARIOS")
        self.StockBT.setText("AGREGAR")
        self.VentaBt.setText("ELIMINAR")
        self.UsuarioBt.setText(" ")
        self.InformeBt.setText("MODIFICAR")
        
        self.frame_central = QFrame()
        self.frame_central.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.verticalLayout_contenido.addWidget(self.frame_central)
        
        self.horizontal_layout = QHBoxLayout(self.frame_central)
        
        # Frame para la tabla
        self.frame_tabla = QFrame()
        self.frame_tabla.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.frame_tabla.setFixedWidth(600)
        self.frame_tabla.setFixedHeight(600)
        
        
        # Layout vertical para los botones del menú
        self.layout_tabla = QVBoxLayout(self.frame_tabla)
       # self.layout_tabla.setSpacing(5)

        self.ingreso_1 = QLineEdit()
        self.ingreso_2 = QLineEdit()
        self.ingreso_3 = QLineEdit()
        self.ingreso_4 = QLineEdit()

        # Etiqueta 2
        self.label_2_titulo = QLabel("USUARIO")
        self.label_2_titulo.setFont(QFont("Arial", 10, QFont.Weight.Bold))  
       # self.label_2_titulo.setStyleSheet("QLabel { margin: -120px; }")

        self.layout_tabla.addWidget(self.label_2_titulo)
        self.layout_tabla.addWidget(self.ingreso_1)

        # Etiqueta 3
        label_3_titulo = QLabel("CONTRASENA")
        label_3_titulo.setFont(QFont("Arial", 10, QFont.Weight.Bold))  
        self.layout_tabla.addWidget(label_3_titulo)
        self.layout_tabla.addWidget(self.ingreso_2)

        # Etiqueta 4
        label_4_titulo = QLabel("NOMBRE Y APELLIDO")
        label_4_titulo.setFont(QFont("Arial", 10, QFont.Weight.Bold))  
    
        self.layout_tabla.addWidget(label_4_titulo)
        self.layout_tabla.addWidget(self.ingreso_3)

        # Etiqueta 5
        label_5_titulo = QLabel("CATEGORIA")
        label_5_titulo.setFont(QFont("Arial", 10, QFont.Weight.Bold))  
        self.layout_tabla.addWidget(label_5_titulo)
        self.layout_tabla.addWidget(self.ingreso_4)
        # Frame para los combo boxes
        self.frame_combo = QFrame()
        self.frame_combo.setStyleSheet("background-color: rgb(135, 206, 235);")

        spacer = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layout_tabla.addItem(spacer)

        
        
        # Layout vertical para los botones del menú
        self.layout_combo = QVBoxLayout(self.frame_combo)

        # Creamos unos QComboBox
        self.combo1 = QComboBox()
        self.combo1.addItems(["OPCION", "Alta", "Baja", "Modificacion"])
        self.combo1.setFixedWidth(150)

        

        # Creamos un QVBoxLayout para los QComboBox
      
        self.layout_combo.addWidget(self.combo1)
        
        self.horizontal_layout.addWidget(self.frame_tabla)
        self.horizontal_layout.addWidget(self.frame_combo)

if __name__ == "__main__":
    app = QApplication([])
    window = VentanaVenta()
    window.show()
    app.exec()
