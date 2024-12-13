import mysql.connector
from mysql.connector import Error
from auxiliares.credenciales_db import config
def DB_insertar(query):
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config)
        if cnx.is_connected():
            cursor = cnx.cursor()
            cursor.execute(query)
            # Confirmar los datos para que queden guardados y no se suban de manera temporal a la bd
            cnx.commit()
            # Obtener el ID de la última fila insertada
            ultimo_id_insertado = cursor.lastrowid
            print("Datos insertados con éxito. ID de la última fila:", ultimo_id_insertado)
            cursor.close()
            cnx.close()

    except Error as e:
        print("Error al conectar con MySQL", e)