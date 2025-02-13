import mysql.connector
import random
import faker

# Configuración de conexión
config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "MinuzaFea265/",
    "database": "local_2024"
}

# Inicializar Faker para generar datos realistas
fake = faker.Faker()

try:
    # Conectar a la base de datos
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Query SQL para insertar clientes
    sql = """
    INSERT INTO clientes (nombre, telefono, email, direccion, id_paquete, ip_cliente, dia_corte, estado)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Lista para almacenar los valores a insertar en lotes
    datos_insertar = []
    
    for _ in range(50):
        nombre = fake.name()
        telefono = f"{random.randint(6000000000, 6999999999)}"  # Número aleatorio con 10 dígitos
        email = nombre.lower().replace(" ", ".") + "@doblenet.com"
        direccion = fake.address().replace("\n", ", ")  # Generar dirección y quitar saltos de línea
        id_paquete = None  # Ahora es NULL en la base de datos
        ip_cliente = f"192.168.1.{random.randint(2, 254)}"
        dia_corte = random.randint(1, 30)
        estado = ("Activo")

        datos_insertar.append((nombre, telefono, email, direccion, id_paquete, ip_cliente, dia_corte, estado))

        # Insertar en lotes de 100 para mayor eficiencia
        if len(datos_insertar) >= 100:
            cursor.executemany(sql, datos_insertar)
            conn.commit()
            datos_insertar = []  # Limpiar lista

    # Insertar cualquier dato restante
    if datos_insertar:
        cursor.executemany(sql, datos_insertar)
        conn.commit()

    print("500 clientes registrados exitosamente con id_paquete NULL.")

except mysql.connector.Error as e:
    print("Error al conectar a MySQL:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
