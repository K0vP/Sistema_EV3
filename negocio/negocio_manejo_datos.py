from datos.insertar_datos_api import DB_insertar
from servicios.obtener_datos_api import ObtenerDatosApi
def Datos(opcion):
    json_datos = ObtenerDatosApi(opcion)
    if opcion == "1":
        for dato in json_datos:  # Itera sobre cada post en la lista
            query = """INSERT INTO posts (id, user_id, title, body) VALUES (%s,%s,%s,%s)"""
            values = dato['id'], dato["userId"], dato["title"], dato["body"]  # Asegúrate de usar 'userId' en lugar de 'user_id'
            DB_insertar(query, values)
    elif opcion == "2":
        for dato in json_datos:  # Itera sobre cada comentario en la lista
            query = """INSERT INTO comments (post_id, id, name, email, body) VALUES (%s,%s,%s,%s,%s)"""
            values = dato["postId"], dato["id"], dato["name"], dato["email"], dato["body"]  # Asegúrate de que estos campos existan en tu respuesta
            DB_insertar(query, values)  # Llama a la función para insertar en la base de datos
    