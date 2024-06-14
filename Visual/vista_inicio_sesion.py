from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class VistaInicioSesion(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.setWindowTitle("Inicio Sesión")
        self.setFixedSize(QSize(400, 600))

        palette = QPalette()
        palette.setColor(
            QPalette.ColorGroup.All, QPalette.ColorRole.Window, QColor(135, 206, 235)
        )  # color de la ventana
        self.setPalette(palette)

        self.contenedor_principal = QVBoxLayout()

        # Frame para la imagen y el título "Cafe Viera"
        self.frame_imagen = QFrame()
        self.frame_imagen.setFixedHeight(100)
        self.contenedor_horizontal = QHBoxLayout(self.frame_imagen)
        self.contenedor_horizontal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.etiqueta_cafe = QLabel()
        self.imagen = QPixmap(
            "C:/Users/Daria/Desktop/Universidad/Cursada_2024/200/220/223_POO/POO_CC/SG_Cafeteria/Visual/imagenes/coffe.png"
        ).scaled(45, 45)
        self.etiqueta_cafe.setPixmap(self.imagen)

        self.etiqueta_nombre = QLabel(" Café Viera", self)
        self.etiqueta_nombre.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.etiqueta_nombre.setStyleSheet(
            "color: white; font-weight: bold; font-size: 40px;"
        )

        self.contenedor_horizontal.addWidget(self.etiqueta_cafe)
        self.contenedor_horizontal.addWidget(self.etiqueta_nombre)

        # Frame para el formulario de inicio de sesión
        self.frame_login = QFrame()
        self.frame_login.setFixedHeight(400)
        self.contenedor_vertical = QVBoxLayout(self.frame_login)
        self.contenedor_vertical.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Bienvenida
        lbl_bienvenida = QLabel("Bienvenid@")
        lbl_bienvenida.setStyleSheet(
            "color: white; font-weight: bold; font-size: 20px;"
        )
        lbl_bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar el texto
        self.contenedor_vertical.addWidget(lbl_bienvenida)
        self.contenedor_vertical.addSpacing(20)

        # Contenedor para usuario
        self.frame_usuario = QFrame()
        self.contenedor_usuario = QVBoxLayout(self.frame_usuario)
        self.contenedor_usuario.setAlignment(Qt.AlignmentFlag.AlignLeft)

        lbl_usuario = QLabel("Usuario")
        lbl_usuario.setStyleSheet("color: white; font-weight: bold; font-size: 20px;")
        lbl_usuario.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Alinear a la izquierda
        self.contenedor_usuario.addWidget(lbl_usuario)
        self.contenedor_usuario.addSpacing(5)  # Espacio entre el label y el QLineEdit

        self.input_usuario = QLineEdit("mgarrison")
        self.input_usuario.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.input_usuario.setStyleSheet("font-size: 14px;")
        self.input_usuario.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )
        self.input_usuario.setFixedWidth(210)
        self.input_usuario.setContentsMargins(10, 0, 0, 0)
        self.contenedor_usuario.addWidget(self.input_usuario)
        self.contenedor_vertical.addWidget(self.frame_usuario)
        self.contenedor_vertical.addSpacing(10)

        # Contenedor para contraseña
        self.frame_contrasena = QFrame()
        self.contenedor_contrasena = QVBoxLayout(self.frame_contrasena)
        self.contenedor_contrasena.setAlignment(Qt.AlignmentFlag.AlignLeft)

        lbl_constrasenia = QLabel("Contraseña")
        lbl_constrasenia.setStyleSheet(
            "color: white; font-weight: bold; font-size: 20px;"
        )
        lbl_constrasenia.setAlignment(
            Qt.AlignmentFlag.AlignLeft
        )  # Alinear a la izquierda
        self.contenedor_contrasena.addWidget(lbl_constrasenia)
        self.contenedor_contrasena.addSpacing(
            5
        )  # Espacio entre el label y el QLineEdit

        self.frame_contrasena_input = QFrame()
        self.contenedor_contrasena_input = QHBoxLayout(self.frame_contrasena_input)
        self.contenedor_contrasena_input.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_contrasenia = QLineEdit("E$8HjHRj)o")
        self.input_contrasenia.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_contrasenia.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.input_contrasenia.setStyleSheet("font-size: 14px;")
        self.input_contrasenia.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )
        self.input_contrasenia.setFixedWidth(200)
        # self.input_contrasenia.setFixedHeight(21)
        self.contenedor_contrasena_input.addWidget(self.input_contrasenia)

        self.imagen_contrasena = QPushButton()  # boton contrasena oculta
        self.imagen_contrasena.setFixedSize(27, 25)
        self.imagen_contrasena_oculta = QPixmap(
            "C://Users//camus//Desktop//SG_Cafeteria//Visual//imagenes//contrasena_oculta"
        ).scaled(30, 25)
        self.imagen_contrasena_visible = QPixmap(
            "C://Users//camus//Desktop//SG_Cafeteria//Visual//imagenes//contrasena_visible"
        ).scaled(30, 25)
        self.imagen_contrasena.setIcon(QIcon(self.imagen_contrasena_oculta))
        self.imagen_contrasena.setIconSize(self.imagen_contrasena_oculta.size())
        self.imagen_contrasena.setStyleSheet(
            "background-color: none; padding-top: 7px; padding-bottom: 5px;"
        )
        self.imagen_contrasena.pressed.connect(controlador.cambio_modo_contrasena)
        self.contrasena_oculta = True

        self.contenedor_contrasena_input.addWidget(
            self.imagen_contrasena, 0, Qt.AlignmentFlag.AlignRight
        )
        self.contenedor_contrasena.addWidget(self.frame_contrasena_input)
        self.contenedor_vertical.addWidget(self.frame_contrasena)
        self.contenedor_vertical.addSpacing(20)

        # Botón Ingresar
        self.iniciar_sesion = QPushButton("Iniciar Sesión")
        self.iniciar_sesion.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )
        self.iniciar_sesion.setFixedWidth(180)
        self.iniciar_sesion.setFixedHeight(40)
        self.iniciar_sesion.setStyleSheet(
            "background-color: white; border-radius: 5px; font-size: 14px; font-weight: bold; margin-left: 80px;"
        )
        self.contenedor_vertical.addWidget(self.iniciar_sesion)
        self.iniciar_sesion.pressed.connect(controlador.valido_entrada)
        self.contenedor_vertical.addSpacing(5)

        # Botón de recuperar contraseña
        self.boton_recuperar_contrasena = QLabel('<a href="#">Recuperar Contraseña</a>')
        self.boton_recuperar_contrasena.setStyleSheet(
            "color: white; font-size: 14px; text-decoration: underline;"
        )
        self.boton_recuperar_contrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boton_recuperar_contrasena.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )
        self.contenedor_vertical.addWidget(self.boton_recuperar_contrasena)
        self.contenedor_vertical.addSpacing(10)

        # Error
        self.frame_error = QFrame()
        # self.frame_error.setFixedHeight(30)
        self.contenedor_error = QVBoxLayout(self.frame_error)
        self.contenedor_error.setContentsMargins(10, 5, 10, 5)

        self.etiqueta_error = QLabel("")
        self.etiqueta_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiqueta_error.setStyleSheet(
            "font-size: 14px; font-weight: bold; color: red;"
        )
        self.contenedor_error.addWidget(self.etiqueta_error)

        # Contenedor Principal
        self.contenedor_principal.addWidget(self.frame_imagen)
        self.contenedor_principal.addWidget(self.frame_login)
        self.contenedor_principal.addWidget(self.frame_error)

        self.setLayout(self.contenedor_principal)

    # Método para asignar mensaje al label de error
    def set_mensaje_error(self, mensaje):
        self.frame_error.setStyleSheet("background-color: white; border-radius: 10px;")
        self.etiqueta_error.setText(mensaje)
