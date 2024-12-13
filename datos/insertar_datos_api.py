import mysql.connector
from mysql.connector import Error
from auxiliares.credenciales_db import config
def DB_insertar(query,values):
    try:
        cnx = mysql.connector.connect(**config)
        if cnx.is_connected():
            print("Conexión exitosa a la base de datos")
            cursor = cnx.cursor()
            cursor.execute(query,values)
            # Confirmar los datos para que queden guardados y no se suban de manera temporal a la bd
            cnx.commit()
            print("Dato insertado con éxito.")
    except Error as e:
        print("Error al conectar con MySQL:", e)
    finally:
        if cnx.is_connected():
            cnx.close()