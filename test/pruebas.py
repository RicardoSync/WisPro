from customtkinter import CTk, CTkComboBox

tipo_equipo = ["Router", "Antena", "ONU", "Otro"]
tipo_estado = ["Rentado", "Vendido", "Propio"]

tipo_equipo_obtenido = "Switch"
estado_equipo_obtenido = "Prestado"

# Insertar en la primera posición (índice 0)
tipo_equipo.insert(0, tipo_equipo_obtenido)
tipo_estado.insert(0, estado_equipo_obtenido)

def panel():
    windows = CTk()
    opciones = CTkComboBox(windows, values=tipo_equipo)
    opciones2 = CTkComboBox(windows, values=tipo_equipo)

    opciones.pack()
    opciones2.pack()

    windows.mainloop()


panel()