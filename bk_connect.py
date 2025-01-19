import mysql.connector
from tkinter import messagebox

def conexionDB():
    try:
        conn = mysql.connector.Connect(
            host="localhost",
            user="cisco",
            password="MinuzaFea265/",
            database="wisp_control"
        )
        return conn
    
    except mysql.connector.Error as err:
        messagebox.showerror("WisPro", f"No podemos establecer conexion al servidor {err}")