import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0" \
            "",
            database="devbase_expotech",
            port=3307
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Erro ao conectar no banco: {e}")
        return None


def fechar_conexao(conn):
    if conn:
        conn.close()