import paramiko
import tkinter as tk
from tkinter import ttk

# Función para conectar a MikroTik y obtener la lista de clientes DHCP
def obtener_clientes_dhcp():
    # Detalles de conexión SSH
    hostname = '192.168.1.70'
    username = 'admin'
    password = 'zerocuatro04'

    # Crear cliente SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conectar al router MikroTik
        client.connect(hostname, username=username, password=password)
        
        # Ejecutar el comando para obtener las concesiones DHCP
        stdin, stdout, stderr = client.exec_command('/ip dhcp-server lease print')
        
        # Leer la salida
        output = stdout.read().decode()

        # Cerrar la conexión
        client.close()

        return output
    except Exception as e:
        print(f"Error al conectar o ejecutar el comando: {e}")
        return None

clientes = obtener_clientes_dhcp()
print(clientes)