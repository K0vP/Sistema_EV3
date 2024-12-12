from requests import request
from servicios.servicio_url import UrlCompleta
def ObtenerPosts():
    direccion = UrlCompleta()
    request.get(direccion)
    return request.get(direccion).json()
