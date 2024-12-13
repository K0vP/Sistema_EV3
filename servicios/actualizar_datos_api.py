import requests as req
from servicios.servicio_url import UrlCompleta
from formularios.formulario_actualizar import FormActulizar
def ActualizarDatosApi(opcion,IdActualizar):
    url = UrlCompleta(opcion)
    id_actualizar = f'{url}/{IdActualizar}'
    dato = FormActulizar(opcion)
    try:
        respuesta = req.put(id_actualizar, json=dato)
        if respuesta.status_code == 200:
            print (f"el codigo de la respuesta es {respuesta.status_code}")
            print("Datos actualizados")
    except:
        print(f"Error al obtener los datos, detalles:",respuesta.text)