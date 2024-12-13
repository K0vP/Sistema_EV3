def subir_datos():
    from negocio.negocio_manejo_datos import Datos
    from datos.insertar_datos_api import DB_insertar
    query = Datos
    DB_insertar(query)