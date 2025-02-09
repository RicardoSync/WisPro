from pathlib import Path
import subprocess
import platform
import json

def enviar_pint(host):
    so = platform.system().lower() #detectamos el sistema operativo

    if so == "windows":
        comando = ["ping", "-n", "1", host]
    else:
        comando = ["ping", "-c", "1", host]

    try:
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if resultado.returncode == 0:
            print(f"✅ {host} está respondiendo.")
            return True
        else:
            print(f"❌ {host} no responde.")
            return False
    except Exception as e:
        print(f"⚠️ Error al hacer ping: {e}")
        return False

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
            print("El host no responde, llamando al modulo de server")
else:
    print("EL archivo no existe, llamar al modulo Configuracion Server")
    #aqui llamamos al modulo para crear la conexion y guardar el archivo