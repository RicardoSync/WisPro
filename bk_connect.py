from tkinter import messagebox
import mysql.connector
import json

# Diccionario con el mapeo de los alias a los valores reales
MAPEO = {
    "servidores_escobedo": "200.234.227.222",  # IP real para 'servidores_escobedo'
    "usuario_escobedo": "cisco",  # Usuario real para 'usuario_escobedo'
    "password_escobed": "MinuzaFea265/"  # Contraseña real para 'password_escobedo'
}

def conexionDB():
    with open("config.json", "r") as j:
        mydata = json.load(j)

        # Reemplaza los alias con los valores reales utilizando el diccionario MAPEO
        host = MAPEO.get(mydata["host"], mydata["host"])  # Si el alias no se encuentra, mantén el valor original
        port = mydata["port"]
        user = MAPEO.get(mydata["user"], mydata["user"])  # Lo mismo para 'user'
        password = MAPEO.get(mydata["password"], mydata["password"])  # Y para 'password'
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
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {err}")
        return False
