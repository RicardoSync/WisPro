from customtkinter import CTkToplevel, CTkLabel, CTkEntry, CTkButton, CTkComboBox
from tkinter import messagebox, END

#librerias
from bk_recursos import colores_ui, imagenes_ui
from bk_insert import insertarPago
from bk_consultas import consultarPaqueteNombre

colores = colores_ui()
iconos = imagenes_ui()

meotodos = ["Efectivo", "Transferencia", "Tarjeta"]

def enviarPago(id_cliente, montoEntry, metodoEntry, cantidadEntry, planActual, panel, nombre_cliente, nombre_admin):
    try:
        monto = float(montoEntry.get())  # Convertir a número
        cantidad = float(cantidadEntry.get())  # Convertir a número
        metodo = metodoEntry.get()
        paquete = planActual.get()

        cambio = cantidad - monto  # No es necesario convertir a `int`, ya que el cambio puede ser decimal
        insertarCambio(id_cliente, monto, metodo, cantidad, panel, cambio, nombre_cliente, paquete, nombre_admin)

    except ValueError:
        messagebox.showerror("SpiderNet", "Error: Ingrese valores numéricos válidos en monto y cantidad")

def insertarCambio(id_cliente, monto, metodo_pago, cantidad ,panel, cambio, nombre_cliente, paquete, nombre_admin):
    cambioLabel = CTkLabel(panel, text="Cambio $", font=("Arial", 18, "bold"), text_color="white")
    cambioEntry  = CTkEntry(panel, border_color=colores["marcos"],
                        border_width=2, corner_radius=10,
                        width=250
                        )
    cambioEntry.delete(0, END)    
    cambioEntry.insert(0, cambio)

    if insertarPago(id_cliente, monto, metodo_pago, cantidad, cambio, nombre_cliente, paquete, nombre_admin):
        print("pago generado")
    else:
        messagebox.showerror("SpiderNet", "No podemos registrar el pago en base de datos")

    cambioLabel.grid(column=1, row=2, padx=10, pady=10)
    cambioEntry.grid(column=1, row=3, padx=10, pady=10)

def insertarElementos(nombre_paquete, planActual, montoEntry):
    precio = consultarPaqueteNombre(nombre_paquete)

    if not precio:
        precio = "Desconocido"
        return None
    planActual.insert(0, nombre_paquete)
    montoEntry.insert(0, precio[0])

def formulario(id_cliente, nombre, nombre_paquete, panel, nombre_admin):
    planActualLabel = CTkLabel(panel, text="Plan Actual", font=("Arial", 18, "bold"), text_color="white")
    planActual  = CTkEntry(panel, border_color=colores["marcos"],
                        border_width=2, corner_radius=10,
                        width=250
                        )
    
    montoLabel = CTkLabel(panel, text="Monto a Pagar", font=("Arial", 18, "bold"), text_color="white")
    montoEntry  = CTkEntry(panel, border_color=colores["marcos"],
                        border_width=2, corner_radius=10,
                        width=250
                        )
    
    cantidadLabel = CTkLabel(panel, text="Dinero Ingresado", font=("Arial", 18, "bold"), text_color="white")
    cantidadEntry  = CTkEntry(panel, border_color=colores["marcos"],
                        border_width=2, corner_radius=10,
                        width=250
                        )
    

    
    metodoLabel = CTkLabel(panel, text="Metodo de Pago", font=("Arial", 18, "bold"), text_color="white")
    metodoEntry  = CTkComboBox(panel, border_color=colores["marcos"],
                        border_width=2, corner_radius=10,
                        values=meotodos,
                        width=250
                        )
    
    btnRegistrar = CTkButton(panel, text="Registrar", border_color=colores["marcos"], border_width=2,
                            corner_radius=10, fg_color=colores["boton"],
                            text_color="black",
                            width=250,
                            #command=lambda:enviarPago(id_cliente, montoEntry, metodoEntry, cantidadEntry, planActual ,panel, nombre_cliente=nombre, nombre_admin))
                            command=lambda:enviarPago(id_cliente, montoEntry, metodoEntry, cantidadEntry, planActual, panel, nombre_cliente=nombre, nombre_admin=nombre_admin)
                            )

    #posicion de los elementos
    planActualLabel.grid(column=0, row=0, padx=10, pady=10)
    montoLabel.grid(column=1, row=0, padx=10, pady=10)
    planActual.grid(column=0, row=1, padx=10, pady=10)
    montoEntry.grid(column=1, row=1, padx=10, pady=10)

    cantidadLabel.grid(column=0, row=2, padx=10, pady=10)
    cantidadEntry.grid(column=0, row=3, padx=10, pady=10)

    metodoLabel.grid(column=0, row=4, padx=10, pady=10)
    metodoEntry.grid(column=0, row=5, padx=10, pady=10)
    btnRegistrar.grid(column=1, row=5, padx=10, pady=10)

    insertarElementos(nombre_paquete, planActual, montoEntry)

def registar_pago(id_cliente, nombre, nombre_paquete, nombre_admin):

    panel = CTkToplevel()
    panel.title(f"Registro de pago {nombre}")
    panel.geometry("600x300")
    panel.resizable(False, False)
    panel.configure(fg_color=colores["fondo"])
    formulario(id_cliente, nombre, nombre_paquete, panel, nombre_admin)

    panel.mainloop()