from PyQt6.QtWidgets import QApplication, QComboBox, QLabel, QPushButton,QHBoxLayout,QVBoxLayout, QWidget, QFrame, QDateTimeEdit,QSizePolicy,QCalendarWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


from ventana_principal import VentanaPrincipal

class VentanaVenta(VentanaPrincipal):
    def __init__(self):
        super().__init__()

        self.BienvenidoLB.setText("INFORMES")
        self.StockBT.setText("VENTAS")
        self.VentaBt.setText("STOCK")
        self.UsuarioBt.setText("IMPRIMIR INFORME")
        self.InformeBt.setText("PEDIDOS")
        
        self.frame_central = QFrame()
        self.frame_central.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.verticalLayout_contenido.addWidget(self.frame_central)
        
        self.horizontal_layout = QHBoxLayout(self.frame_central)
        
        # Frame para la tabla (permanecerá vacío)
        self.frame_tabla = QFrame()
        self.frame_tabla.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.frame_tabla.setFixedWidth(600)
        self.frame_tabla.setFixedHeight(600)

        self.layout_tabla = QVBoxLayout(self.frame_tabla)

        # Etiqueta 1
        label_1_titulo = QLabel("FECHA")
        label_1_titulo.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_1_titulo.setFont(QFont("Arial", 10, QFont.Weight.Bold))  
        label_1_valor = QLabel("")
        self.layout_tabla.addWidget(label_1_titulo)
        self.layout_tabla.addWidget(label_1_valor)

        # Etiqueta 2
        label_2_titulo = QLabel("TITULO")
        label_2_titulo.setFont(QFont("Arial", 10, QFont.Weight.Bold))  
        label_2_valor = QLabel("")
        self.layout_tabla.addWidget(label_2_titulo)
        self.layout_tabla.addWidget(label_2_valor)

        # Etiqueta 3
        label_3_titulo = QLabel("DATOS")
        label_3_titulo.setFont(QFont("Arial", 10, QFont.Weight.Bold))  
        label_3_valor = QLabel("")
        self.layout_tabla.addWidget(label_3_titulo)
        self.layout_tabla.addWidget(label_3_valor)

        # Etiqueta 4
        label_4_titulo = QLabel("ANALISIS")
        label_4_titulo.setFont(QFont("Arial", 10, QFont.Weight.Bold))  
        label_4_valor = QLabel("")
        self.layout_tabla.addWidget(label_4_titulo)
        self.layout_tabla.addWidget(label_4_valor)

        # Etiqueta 5
        label_5_titulo = QLabel("CONCLUSIONES")
        label_5_titulo.setFont(QFont("Arial", 10, QFont.Weight.Bold))  
        label_5_valor = QLabel("")
        self.layout_tabla.addWidget(label_5_titulo)
        self.layout_tabla.addWidget(label_5_valor)
   
        self.historialBT = QPushButton("HISTORIAL")
        self.historialBT.setFixedWidth(150) 
        self.historialBT.setFixedHeight(50)         
        self.layout_tabla.addWidget(self.historialBT)

        
        # Frame para los combo boxes
        self.frame_combo = QFrame()
        self.frame_combo.setStyleSheet("background-color: rgb(135, 206, 235);")
        
        # Layout vertical para los botones del menú
        self.layout_combo = QVBoxLayout(self.frame_combo)
        self.layout_combo.setSpacing(5)  # Reducimos el espacio entre los elementos
        self.layout_combo.setContentsMargins(0, 0, 0, 0)
        

        # Creamos unos QComboBox
        self.label_fechadesde = QLabel("FECHA DESDE")
        self.label_fechadesde.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
     
        self.combo1 = QCalendarWidget()
        self.combo1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.label_fechahasta = QLabel("FECHA HASTA")
        self.label_fechahasta.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.combo2 = QCalendarWidget()
        self.combo2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        
       

        # Creamos un QVBoxLayout para los QComboBox
        self.layout_combo.addWidget(self.label_fechadesde)
        self.layout_combo.addWidget(self.combo1)
        self.layout_combo.addWidget(self.label_fechahasta)
        self.layout_combo.addWidget(self.combo2)
        
        #self.layout_combo.addSpacing(20)

        self.horizontal_layout.addWidget(self.frame_tabla)  # Espacio reservado para la tabla, pero no se muestra
        self.horizontal_layout.addWidget(self.frame_combo)

    

if __name__ == "__main__":
    app = QApplication([])
    window = VentanaVenta()
    window.show()
    app.exec()
