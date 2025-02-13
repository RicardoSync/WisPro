from pathlib import Path
import subprocess
import platform
from tkinter import messagebox

def enviar_pint(host, repeticiones):
    so = platform.system().lower() #detectamos el sistema operativo

    if so == "windows":
        comando = ["ping", "-n", f"{repeticiones}", host]
    else:
        comando = ["ping", "-c", f"{repeticiones}", host]

    try:
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if resultado.returncode == 0:
            print(f"✅ {host} está respondiendo.")
            return True
        else:
            print(f"❌ {host} no responde.")
            return False
    except Exception as e:
        messagebox.showerror("SpiderNet", f"⚠️ Error al hacer ping: {e}")
        return False