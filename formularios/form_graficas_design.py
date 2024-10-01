# Autor: Jonathan Hernández
# Fecha: 30 Septiembre 2024
# Descripción: Código para GUI MODERNA PYTHON.
# GitHub: https://github.com/Jona163

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FormularioGraficasDesign():

    def __init__(self, panel_principal):           
        # Crear dos subgráficos usando Matplotlib
        figura = Figure(figsize=(8, 6), dpi=100)
        ax1 = figura.add_subplot(211)
        ax2 = figura.add_subplot(212)                
        
        # Ajustar la distribución para agregar espacio de separación en el eje Y
        figura.subplots_adjust(hspace=0.4)

        # Graficar en los subgráficos
        self.grafico1(ax1)
        self.grafico2(ax2)

        # Agregar los gráficos a la ventana de Tkinter
        canvas = FigureCanvasTkAgg(figura, master=panel_principal)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    def grafico1(self, ax):
        # Función para graficar el primer conjunto de datos como un gráfico de barras
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

        # Cambiar a un gráfico de barras
        ax.bar(x, y, label='Gráfico 1', color='blue', alpha=0.7)

        # Personalizar el aspecto del gráfico
        ax.set_title('Gráfico 1 - Gráfico de Barras')
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.legend()
