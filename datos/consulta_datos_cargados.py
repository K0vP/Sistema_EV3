from auxiliares.credenciales_db import config
from auxiliares.constantes import visualizar
import mysql.connector 
def DB_consulta(opcion): 
    cnx = None
    cursor = None
    query =f"""SELECT * FROM {visualizar[opcion]}"""    
    try:  
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                cursor.execute(query)
                # Obtener y mostrar los nombres de las columnas
                columnas = [desc[0] for desc in cursor.description]
                print(" | ".join(columnas))  # Imprime los nombres de las columnas
                print("-" * 50)  # Línea separadora
        
                # Obtener los resultados
                rows = cursor.fetchall()
                for row in rows:
                    print(" | ".join(map(str, row)))# Convertir cada valor a cadena y unir
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()