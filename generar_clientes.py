import mysql.connector
import random
import faker
from bk_connect import conexionDB

def generar_clientes(numero_clientes):
    # Inicializar Faker para generar datos realistas
    fake = faker.Faker()

    try:
        # Conectar a la base de datos
        conn = conexionDB()
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
            telefono = f"{random.randint(1000000000, 6999999999)}"  # Número aleatorio con 10 dígitos
            email = nombre.lower().replace(" ", ".") + "@doblenet.com"
            direccion = fake.address().replace("\n", ", ")  # Generar dirección y quitar saltos de línea
            id_paquete = None  # Ahora es NULL en la base de datos
            ip_cliente = f"192.168.1.{random.randint(2, 254)}"
            dia_corte = random.randint(1, 30)
            estado = ("Activo")

            datos_insertar.append((nombre, telefono, email, direccion, id_paquete, ip_cliente, dia_corte, estado))

            # Insertar en lotes de 100 para mayor eficiencia
            if len(datos_insertar) >= numero_clientes:
                cursor.executemany(sql, datos_insertar)
                conn.commit()
                datos_insertar = []  # Limpiar lista

        # Insertar cualquier dato restante
        if datos_insertar:
            cursor.executemany(sql, datos_insertar)
            conn.commit()

        return True

    except mysql.connector.Error as e:
        print("Error al conectar a MySQL:", e)
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
