from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QStackedWidget, QTableWidget
from PyQt6 import QtCore


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1048, 680)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        
        # Layout principal 
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.layout.setSpacing(0)
        
        # Frame superior
        self.frame_superior = QFrame()
        self.frame_superior.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.frame_superior.setFixedHeight(50)
        self.layout.addWidget(self.frame_superior)
        
        # Layout para el contenido y el menú
        self.horizontalLayout = QHBoxLayout()
        self.layout.addLayout(self.horizontalLayout)
      
        
        # Frame para el menú
        self.frame_menu = QFrame()
        self.frame_menu.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.frame_menu.setFixedWidth(200)
        self.horizontalLayout.addWidget(self.frame_menu) 
        
        # Layout vertical para los botones del menú
        self.verticalLayout_menu = QVBoxLayout(self.frame_menu)
        self.verticalLayout_menu.setContentsMargins(10, 10, 10, 10)
        
        # Botones del menú
        self.StockBT = QPushButton("STOCK")
        self.StockBT.setMinimumHeight(40)
        self.verticalLayout_menu.addWidget(self.StockBT)
        
        self.VentaBt = QPushButton("VENTA")
        self.VentaBt.setMinimumHeight(40)
        self.verticalLayout_menu.addWidget(self.VentaBt)
        
        self.InformeBt = QPushButton("INFORME")
        self.InformeBt.setMinimumHeight(40)
        self.verticalLayout_menu.addWidget(self.InformeBt)
        
        self.UsuarioBt = QPushButton("PRODUCTO")
        self.UsuarioBt.setMinimumHeight(40)
        self.verticalLayout_menu.addWidget(self.UsuarioBt)
        
        # Frame para el contenido principal
        self.frame_contenido = QFrame()
        self.horizontalLayout.addWidget(self.frame_contenido)
        
        # Layout vertical para el contenido principal
        self.verticalLayout_contenido = QVBoxLayout(self.frame_contenido)
        self.verticalLayout_contenido.setContentsMargins(10, 10, 10, 10)
        
        # Label de bienvenida
        self.BienvenidoLB = QLabel("BIENVENIDO")
        self.BienvenidoLB.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_contenido.addWidget(self.BienvenidoLB)
        """
        # Tabla de contenido
        self.tabla_contenido = QTableWidget()
        self.verticalLayout_contenido.addWidget(self.tabla_contenido)
        """
if __name__ == "__main__":
    app = QApplication([])
    window = VentanaPrincipal()
    window.show()
    app.exec()
