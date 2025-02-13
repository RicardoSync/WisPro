from pathlib import Path
import subprocess
import platform
import json
from tkinter import messagebox
from bk_ping import enviar_pint
from md_registro import md_registro_windows

configuracion = Path("config.json") #le indicamos que archivo

if configuracion.exists():
    #si existe obtenemos la ip para mandar ping. Si responde llamamos al modulo Login
    #caso de no responder llamamos al modulo de server
    print("Archivo existe, llamar a ping del host")
    
    with open(configuracion, "r") as j: #abrimos el json en formato de lectura
        mydata = json.load(j) 
        host = mydata["host"]
        ping_exitoso = enviar_pint(host)

        if ping_exitoso:
            print("Llamando al modulo de login")
            from md_login import inicioSesion
            inicioSesion()
        else:
            messagebox.showwarning("SpiderNet", f"""No podemos establecer conexion con el servidor.\nEn caso de que uses el servicio online de Software Escobedo, verifica tu conexion a internet.\nSi usas tu propio servidor local o en la nube verifica que estes dentro de la misma red que tu host {host}.\nSi el problema persiste o no encuentras la solucion contacta con nosotros al numero +5214981442266""")

else:
    """
    Aqui si el archivo.json no existe entonces llamamos al modulo para configurar las credenciales, host y generar la base de datos
    """
    print("llamando al modulo")
    md_registro_windows()