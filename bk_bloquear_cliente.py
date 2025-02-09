import paramiko
from tkinter import messagebox
from bk_update import actualizar_bloqueo, actualizar_desbloqueo

def bloquear_ip(host, user, password, ip_bloqueo, id):
    try:
        # Iniciar conexión SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password)

        # Comando para bloquear la IP en DHCP
        command = f"/ip dhcp-server lease set [find address={ip_bloqueo}] block-access=yes"

        # Ejecutar el comando
        stdin, stdout, stderr = client.exec_command(command)

        # Mostrar salida del comando
        print(stdout.read().decode())


        bloqueo = actualizar_bloqueo(id)
        if bloqueo:
            # Cerrar conexión
            client.close()
            return True
        else:
            client.close()


    except Exception as e:
        messagebox.showerror("SpiderNet", f"Error al bloquear la IP: {e}")

def desbloquear_ip(host, user, password, ip_bloqueo, id):
    try:
        # Iniciar conexión SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password)

        # Comando para bloquear la IP en DHCP
        command = f"/ip dhcp-server lease set [find address={ip_bloqueo}] block-access=no"

        # Ejecutar el comando
        stdin, stdout, stderr = client.exec_command(command)

        # Mostrar salida del comando
        print(stdout.read().decode())
        
        desbloqueo = actualizar_desbloqueo(id)
        if desbloqueo:
            # Cerrar conexión
            client.close()
            return True
        else:
            client.close()

    except Exception as e:
                messagebox.showerror("SpiderNet", f"Error al desbloquear la IP: {e}")

def bloquear_clientes_ips(host, user, password, ip_bloqueo, id_cliente):
    try:
        # Iniciar conexión SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password)

        # Comando para bloquear la IP en DHCP
        command = f"/ip dhcp-server lease set [find address={ip_bloqueo}] block-access=yes"

        # Ejecutar el comando
        stdin, stdout, stderr = client.exec_command(command)

        # Mostrar salida del comando
        print(stdout.read().decode())

        # Actualizar el estado de bloqueo en la BD
        bloqueo = actualizar_bloqueo(id_cliente)

        client.close()  # Cerrar conexión SSH después de usarla
        return bloqueo

    except Exception as e:
        print(f"Error al bloquear la IP {ip_bloqueo}: {e}")
        return False

def desbloquear_clientes_ips(host, user, password, ip_bloqueo, id_cliente):
    try:
        # Iniciar conexión SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password)

        # Comando para bloquear la IP en DHCP
        command = f"/ip dhcp-server lease set [find address={ip_bloqueo}] block-access=no"

        # Ejecutar el comando
        stdin, stdout, stderr = client.exec_command(command)

        # Mostrar salida del comando
        print(stdout.read().decode())

        # Actualizar el estado de bloqueo en la BD
        bloqueo = actualizar_desbloqueo(id_cliente)

        client.close()  # Cerrar conexión SSH después de usarla
        return bloqueo

    except Exception as e:
        print(f"Error al bloquear la IP {ip_bloqueo}: {e}")
        return False
