from customtkinter import CTk, CTkComboBox

# Crear una lista de los días del 1 al 31 (como cadenas de texto)
dias_corte = [str(day) for day in range(1, 32)]

# Crear ventana
windows = CTk()
windows.title("Días de Corte")

# Crear ComboBox con la lista de días
dias = CTkComboBox(windows, values=dias_corte)

# Mostrar ComboBox en la ventana
dias.pack()

# Iniciar el loop de la interfaz gráfica
windows.mainloop()
