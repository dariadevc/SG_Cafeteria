from Visual.vista_jefe import VistaJefe


class ControladorJefe:
    
    def __init__(self):
        self.__vista_jefe = VistaJefe(self)
        self.__vista_jefe.show()