import json
import customtkinter as ctk

# Función para cargar configuración
def cargar_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Función para guardar configuración
def guardar_config():
    nueva_config = {
        "host": entry_host.get(),
        "port": int(entry_port.get()),
        "user": entry_user.get(),
        "password": entry_password.get(),
        "database": entry_database.get()
    }
    
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(nueva_config, file, indent=4)
    
    label_status.configure(text="✔ Configuración guardada", text_color="green")

# Cargar valores iniciales
config = cargar_config()

# Configurar la ventana principal
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Configuración de MySQL")
root.geometry("400x350")

# Crear etiquetas y entradas
ctk.CTkLabel(root, text="Host:").pack(pady=(10, 0))
entry_host = ctk.CTkEntry(root, width=300)
entry_host.pack()
entry_host.insert(0, config["host"])

ctk.CTkLabel(root, text="Puerto:").pack(pady=(10, 0))
entry_port = ctk.CTkEntry(root, width=300)
entry_port.pack()
entry_port.insert(0, str(config["port"]))

ctk.CTkLabel(root, text="Usuario:").pack(pady=(10, 0))
entry_user = ctk.CTkEntry(root, width=300)
entry_user.pack()
entry_user.insert(0, config["user"])

ctk.CTkLabel(root, text="Contraseña:").pack(pady=(10, 0))
entry_password = ctk.CTkEntry(root, width=300, show="*")  # Oculta la contraseña
entry_password.pack()
entry_password.insert(0, config["password"])

ctk.CTkLabel(root, text="Base de Datos:").pack(pady=(10, 0))
entry_database = ctk.CTkEntry(root, width=300)
entry_database.pack()
entry_database.insert(0, config["database"])

# Botón para guardar cambios
btn_guardar = ctk.CTkButton(root, text="Guardar", command=guardar_config)
btn_guardar.pack(pady=20)

# Etiqueta de estado
label_status = ctk.CTkLabel(root, text="", text_color="white")
label_status.pack()

root.mainloop()
