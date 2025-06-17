import tkinter
import tkinter.messagebox as messagebox

def entrada_general(formulario, tablas, actualicion):
    labels_texts = [
        "ᴇʟ ᴄᴏʟᴏʀ:",
        "ʜᴏʀᴀ ᴅᴇ ɪɴɪᴄɪᴏ:",
        "ʜᴏʀᴀ ᴅᴇ ꜰɪɴᴀʟɪᴢᴀᴄɪᴏɴ:",
        "ʟᴀ ᴘʟᴀᴄᴀ:",
        "ɢᴇɴᴇʀᴏ:"
    ]
    entries = {}

    contenedor = tkinter.Frame(formulario, bg="white")
    contenedor.pack(fill="both", expand=True, padx=20, pady=20)

    for texto in labels_texts:
        lbl = tkinter.Label(contenedor, text=texto, bg="white", anchor="w", font=("Arial", 10, "bold"))
        lbl.pack(pady=5, fill="x")
        ent = tkinter.Entry(contenedor, bd=1, relief="solid")
        ent.pack(pady=5, fill="x")
        entries[texto] = ent

    def boton_filtrar():
        color = entries["ᴇʟ ᴄᴏʟᴏʀ:"].get().strip()
        tiempo_inicio = entries["ʜᴏʀᴀ ᴅᴇ ɪɴɪᴄɪᴏ:"].get().strip()
        tiempo_fin = entries["ʜᴏʀᴀ ᴅᴇ ꜰɪɴᴀʟɪᴢᴀᴄɪᴏɴ:"].get().strip()
        placa = entries["ʟᴀ ᴘʟᴀᴄᴀ:"].get().strip()
        genero = entries["ɢᴇɴᴇʀᴏ:"].get().strip()

        condiciones = []

        if color:
            condiciones.append(f"color = '{color}'")

        if tiempo_inicio and tiempo_fin:
            if not tiempo_inicio.isdigit() or not tiempo_fin.isdigit():
                messagebox.showerror("Error", "Los valores de tiempo únicamente pueden ser numéricos")
                return
            h1 = int(tiempo_inicio)
            h2 = int(tiempo_fin)
            if h1 > h2:
                messagebox.showerror("Error", "El tiempo inicio no puede ser mayor que el tiempo fin")
                return
            hora1 = f"{h1:02d}:00"
            hora2 = f"{h2:02d}:00"
            condiciones.append(f"(hora_entrada BETWEEN '{hora1}' AND '{hora2}')")

        elif tiempo_inicio or tiempo_fin:
            messagebox.showerror("Error", "Ambos campos de tiempo deben estar llenos")
            return

        if placa:
            condiciones.append(f"placa = '{placa}'")

        if genero:
            condiciones.append(f"genero = '{genero}'")

        consulta = "SELECT * FROM control"
        if condiciones:
            consulta += " WHERE " + " AND ".join(condiciones)

        print(f"Consulta SQL generada: {consulta}")

        actualicion(consulta, tablas)

    boton = tkinter.Button(contenedor, text="Actualizar", command=boton_filtrar)
    boton.pack(pady=10)

    return entries, boton