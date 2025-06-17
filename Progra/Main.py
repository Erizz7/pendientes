import tkinter as TK
from Vistas.Encabezado import encabezado
from Vistas.Tablas_Formulas import a

ventana = TK.Tk()
ventana.title("BASE DE DATOS ESTACIONAMIENTO")
ventana.geometry("1200x700")

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=6)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=6)

encabezado(ventana)
a(ventana)
(ventana)

ventana.mainloop()