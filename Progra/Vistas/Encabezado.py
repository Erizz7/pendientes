import tkinter
from tkinter import font
from PIL import Image, ImageTk

def encabezado(ventana):
    try:
        panel_encabezado = tkinter.Frame(ventana, bg="lightgreen", width=1000, height=100)
        panel_encabezado.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Subcontenedor centrado
        contenedor_central = tkinter.Frame(panel_encabezado, bg="lightgreen")
        contenedor_central.place(relx=0.5, rely=0.5, anchor="center")

        # Imagen
        imagen = Image.open(r"C:\Users\dell\OneDrive\Escritorio\Progra\logo.png")
        imagen = imagen.resize((80, 80))  # Tamaño más discreto si va centrado
        logo = ImageTk.PhotoImage(imagen)

        etiqueta_logo = tkinter.Label(contenedor_central, image=logo, bg="lightgreen", bd=0)
        etiqueta_logo.image = logo
        etiqueta_logo.pack(side="left", padx=10)

        # Texto
        tipodeletra = font.Font(family="Arial", size=16, weight="bold")
        titulo = tkinter.Label(contenedor_central, text="C O N T R O L", font=tipodeletra, bg="lightgreen")
        titulo.pack(side="left", padx=10)

    except Exception as e:
        print("Error en encabezado():", e)