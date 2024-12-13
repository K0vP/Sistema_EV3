from auxiliares.credenciales_db import config 
import mysql.connector
def iniciar_db():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios_api(id_usuario_api int PRIMARY key);""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS posts (id INT PRIMARY KEY,user_id INT,title varchar(200), body VARCHAR(200),FOREIGN KEY (user_id) REFERENCES usuarios_api (id_usuario_api));""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS comments(post_id INT,id INT,name VARCHAR(150),email VARCHAR(50),body VARCHAR(200));""")
    
    cursor.close()
    cnx.close()
    print ("Base de datos iniciada")
