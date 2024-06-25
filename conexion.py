import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, port,  db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            port = port,
            database=db_name
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        
create_connection("localhost", "root", "", "3306" ,"inmobiliaria")


