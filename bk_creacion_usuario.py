from bk_connect import conexionDB
from tkinter import messagebox
#admin = 0
#tecnico = 1
#cajero = 2

def insertarUsuario(nombre, usuario, password, tipo_usuario):
    
    try:
        rol = None

        if tipo_usuario == "admin":
            rol = 0
        elif tipo_usuario == "tecnico":
            rol = 1
        elif tipo_usuario == "cajero":
            rol = 2
        else:
            messagebox.showerror("WisPro", f"No reconocemos el rol, intenta de nuevo con uno valido :)")
        
        conn = conexionDB()
        cursor = conn.cursor()
        sql = """
        INSERT INTO usuarios (nombre, usuario, password, rol) VALUES  (%s,%s,%s,%s)"""
        valores = (nombre, usuario, password, rol)
        cursor.execute(sql, valores)

        conn.commit()

        conn.close()
        cursor.close()
        messagebox.showinfo("WisPro", f"Se creo de manera correcta el usuario {usuario}, ahora inicia sesion")
        #return "Exito"
    
    except Exception as err:
        messagebox.showerror("WisPro", f"No podemos crear el usuario {err}")

