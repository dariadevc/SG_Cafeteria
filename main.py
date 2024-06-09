import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append('C://Users//camus//Desktop//SG_Cafeteria//Controlador')
from Controlador.controlador_inicio import ControladorInicioSesion
from PyQt6.QtWidgets import QApplication


# sys.path.append('C://Users//camus//Desktop//SG_Cafeteria//Controlador')


app = QApplication(sys.argv)
window = ControladorInicioSesion()
app.exec()


## Datos inicio sesión
## mgarrison
## E$8HjHRj)o
