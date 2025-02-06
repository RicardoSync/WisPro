import paramiko

def prueba_conexion(mikrotik_ip, port, username, password):
    try:
        # Crear objeto cliente SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Aceptar clave automáticamente

        # Intentar conectar
        ssh.connect(mikrotik_ip, port=port, username=username, password=password, timeout=5)

        # Ejecutar un comando de prueba en el MikroTik
        stdin, stdout, stderr = ssh.exec_command("system identity print")

        # Mostrar la salida del comando
        print(stdout.read().decode())

        # Cerrar conexión
        ssh.close()
        return True
    
    except paramiko.AuthenticationException:
        print("Error de autenticación: Verifica tu usuario y contraseña.")
    except paramiko.SSHException as e:
        print(f"Error en la conexión SSH: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
