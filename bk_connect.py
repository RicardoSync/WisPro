from tkinter import messagebox
import mysql.connector

def conexionDB():
    try:
        conn = mysql.connector.Connect(
            host="localhost",
            user="root",
            password="MinuzaFea265/",
            database="wisp_control"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("SpiderNet", f"No podemos establecer la comunicacion {err}")