import requests as req
from servicios.servicio_url import UrlCompleta
from auxiliares.constantes import visualizar
def eliminar_registro_api(opcion):
    if opcion in visualizar:
        id_registro = input(f"Ingrese el id del {visualizar[opcion]} que desea eliminar:")
    url = UrlCompleta(opcion)
    delete =f"{url}/{id_registro}" 
    respuesta = req.delete(delete)
    
    if respuesta.status_code == 200:
        print(f"Registro con ID {id_registro} eliminado correctamente.")
        print (f"el codigo de la respuesta es {respuesta.status_code}")
        return respuesta.json()
    else:
        print(f"Error al eliminar el registro. Código de estado: {respuesta.status_code}")
        return None