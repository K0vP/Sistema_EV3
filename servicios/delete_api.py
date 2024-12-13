import requests as req

def eliminar_registro_api(url_base, recurso, id_registro):
    url = f"{url_base}/{recurso}/{id_registro}"
    respuesta = req.delete(url)
    
    if respuesta.status_code == 200:
        print(f"Registro con ID {id_registro} eliminado correctamente.")
        return respuesta.json()
    else:
        print(f"Error al eliminar el registro. Código de estado: {respuesta.status_code}")
        return None

url_base = "https://jsonplaceholder.typicode.com"
recurso = "posts"
id_registro = 1
respuesta = eliminar_registro_api(url_base, recurso, id_registro)
print(respuesta)
