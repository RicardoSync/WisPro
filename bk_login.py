from bk_connect import conexionDB


def comprobacion(usuario, password):
    try:
        conn = conexionDB()
        cursor = conn.cursor()
        sql = "SELECT usuario, rol FROM usuarios WHERE usuario = %s AND password = %s"
        valores = (usuario, password)