from servicios.obtener_datos_api import ObtenerDatosApi
import json
def Datos(opcion):
    json_datos = ObtenerDatosApi(opcion)
    datos = json.loads(json_datos)
    if opcion == "1":
        query = """INSERT INTO posts (id, user_id, title, body) VALUES (?,?,?,?)""",(datos['id'],datos["userid"],datos["tittle"],datos["body"])
        return query
    elif opcion == "2":
        query = """INSERT INTO comments (post_id, id, name, email, body) VALUES (?,?,?,?,?)""",(datos["post_id"],datos["id"],datos["name"],datos["email"],datos["body"])
        return query
    