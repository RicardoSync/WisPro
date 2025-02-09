import subprocess
import ipaddress

# Dirección IP de inicio y máscara de red
network = ipaddress.IPv4Network('122.122.123.0/24', strict=False)

# Función para hacer ping a una IP
def ping(ip):
    response = subprocess.run(
        ['ping', '-c', '1', str(ip)],  # '-c 1' hace un solo ping
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Si el ping fue exitoso (código de salida 0), se imprime la IP
    if response.returncode == 0:
        print(f'IP {ip} está activa.')
    else:
        print(f'IP {ip} no responde.')

# Iterar sobre el rango de IPs y hacer ping
for ip in network.hosts():
    ping(ip)
