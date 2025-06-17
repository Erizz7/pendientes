import tkinter
from Vistas.Vista_De_Datos import actualicion
from Vistas.Entradas import entrada_general

print("- - Ejecutando Tabla de Formulas - -")

def a(ventana):
    formulario = tkinter.Frame(ventana, bg="white", width=600, height=600)
    formulario.grid(row=1, column=0, sticky="nsew")

    tablas = tkinter.Frame(ventana, bg="#d4f4dd", width=400, height=600)
    tablas.grid(row=1, column=1, sticky="nsew")

    entrada_general(formulario, tablas, actualicion)
    actualicion("SELECT * FROM control", tablas)