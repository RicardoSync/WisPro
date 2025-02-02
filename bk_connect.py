from tkinter import messagebox
import mysql.connector
import json 

def conexionDB():
    with open("config.json", "r") as j:
        mydata = json.load(j)

        host = mydata["host"]
        port = mydata["port"]
        user = mydata["user"]
        password = mydata["password"]
        database = mydata["database"]

    try:
        conn = mysql.connector.Connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        return conn
    
    except mysql.connector.Error as err:
        messagebox.showerror("SpiderNet", f"Error critica al establecer conexion con el servidor {err}")