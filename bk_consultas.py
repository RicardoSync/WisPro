from bk_connect import conexionDB
from tkinter import messagebox

def consultaUsuarios():
    try:
        conn = conexionDB()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, usuario, password, rol FROM usuarios")
        usuarios = cursor.fetchall()

        cursor.close()
        conn.close()

        return usuarios
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos realizar la consulta de los usuarios {err}")