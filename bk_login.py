from bk_connect import conexionDB
from tkinter import messagebox

def login(username, password):
    try:
        conn = conexionDB()
        cursor = conn.cursor()
        sql = """SELECT id, usuario, password, rol FROM usuarios WHERE usuario = %s AND password = %s"""
        valores = (username, password)
        cursor.execute(sql, valores)

        credenciales = cursor.fetchall()

        cursor.close()
        conn.close()

        return credenciales[0]
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos iniciar sesion {err}")