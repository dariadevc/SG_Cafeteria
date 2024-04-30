from Controlador.controlador_inicio import ControladorInicioSesion
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = ControladorInicioSesion()
app.exec()
