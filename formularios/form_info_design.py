# Autor: Jonathan Hernández
# Fecha: 30 Septiembre 2024
# Descripción: Código para GUI MODERNA PYTHON.
# GitHub: https://github.com/Jona163

import tkinter as tk
from typing_extensions import Literal
import util.util_ventana as util_ventana

class FormularioInfoDesign(tk.Toplevel):

    def __init__(self) -> None:
        super().__init__()
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Python GUI')
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 400, 100        
        util_ventana.centrar_ventana(self, w, h)     
