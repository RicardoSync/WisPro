from bk_connect import conexionDB
from tkinter import messagebox

def comprobacion(usuario, password):
    try:
        conn = conexionDB()
        cursor = conn.cursor()
        sql = """
        SELECT usuario, rol FROM usuarios WHERE usuario = %s AND password = %s"""
        valores = (usuario, password)
        cursor.execute(sql, valores)

        credenciales = cursor.fetchall()

        cursor.close()
        conn.close()

        return credenciales[0]
    
    except Exception as err:
        messagebox.showerror("WisPro", f"Hubo un error en las credenciales, intenta nuevamente {err}")