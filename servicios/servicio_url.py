import requests
from auxiliares.urls import Url
from auxiliares.constantes import visualizar
def UrlCompleta(opcion):
    direccion = f"{Url}{visualizar[opcion]}"
    return direccion