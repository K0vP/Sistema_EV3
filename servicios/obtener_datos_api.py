import requests as req
from servicios.servicio_url import UrlCompleta

def ObtenerDatosApi(opcion) :
    url = UrlCompleta(opcion)
    try:
        respuesta = req.get(url)
        if respuesta.status_code == 200:
            print (f"el codigo de la respuesta es {respuesta.status_code}")
            return respuesta.json()
    except:
        print(f"Error al obtener los datos, detalles:",respuesta.text)
