import tkinter
from tkinter import ttk
from Servicio.SQL import conectar

def estilo_tabla():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("A.Treeview.Heading", background="white", foreground="black", font=("Arial", 10, "bold"), relief="flat")
    style.configure("A.Treeview", background="white", foreground="black", fieldbackground="white", borderwidth=2)
    style.map("A.Treeview", background=[("selected", "blue")], foreground=[("selected", "white")])

def actualicion(consulta_sql, panel):
    estilo_tabla()

    datos = conectar(consulta_sql)
    for widget in panel.winfo_children():
        widget.destroy()

    columnas = ("ID", "Nombre", "Genero", "Placa", "Color", "Modelo", "Hora Entrada", "Hora Salida", "Tarifa", "Carwash")
    vista_vertical(panel, columnas, datos)

def vista_vertical(panel, columnas, datos):
    canvas = tkinter.Canvas(panel, bg="white")
    scrollbar = tkinter.Scrollbar(panel, orient="vertical", command=canvas.yview)
    frame_datos = tkinter.Frame(canvas, bg="white")

    frame_datos.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=frame_datos, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    if not datos:
        label = tkinter.Label(frame_datos, text="No se encontraron datos.", fg="red", bg="white", font=("Arial", 12))
        label.pack(pady=5)
        return

    for fila in datos:
        contenedor = tkinter.Frame(frame_datos, bg="#d4f4dd", bd=1, relief="solid")
        contenedor.pack(padx=10, pady=5, fill="x")

        for i, valor in enumerate(fila):
            etiqueta = tkinter.Label(contenedor, text=f"{columnas[i]}: {valor}", bg="#d4f4dd", anchor="w", font=("Arial", 10))
            etiqueta.pack(fill="x", padx=10, pady=2)

def vista_vertical(panel, columnas, datos):
    canvas = tkinter.Canvas(panel, bg="white")
    scrollbar = tkinter.Scrollbar(panel, orient="vertical", command=canvas.yview)
    frame_contenedor = tkinter.Frame(canvas, bg="white")

    frame_contenedor.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=frame_contenedor, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    encabezado = tkinter.Frame(frame_contenedor, bg="white")
    encabezado.pack(pady=10)

    titulo_label = tkinter.Label(encabezado, text="BASE DE DATOS", bg="white", fg="black", font=("Arial", 16, "bold"))
    titulo_label.pack()

    if not datos:
        label = tkinter.Label(frame_contenedor, text="No se encontraron datos.", fg="red", bg="white", font=("Arial", 12))
        label.pack(pady=5)
        return

    for fila in datos:
        fila_frame = tkinter.Frame(frame_contenedor, bg="#d4f4dd", bd=1, relief="solid")
        fila_frame.pack(padx=10, pady=5, fill="x")

        for i, valor in enumerate(fila):
            campo = f"{columnas[i]}: {valor}"
            etiqueta = tkinter.Label(fila_frame, text=campo, bg="#d4f4dd", font=("Arial", 10), anchor="w")
            etiqueta.pack(side="left", padx=10, pady=5)