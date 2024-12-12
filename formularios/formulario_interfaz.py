from auxiliares.constantes import visualizar
from servicios.obtener_datos_api import ObtenerDatosApi
def menu ():
    print('Bienvenido')
    realizar = input('Que desea relaizar:\n1: Consultar\n2: Crear\n3: Editar\n4: Eliminar\nIngrese el numero de la opcion: ')
    if realizar == '1':
        opcion_consultar = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\nIngrese el numero de la opcion: ')
        if opcion_consultar in [visualizar]:
            print (f'Selecciono la opcion {visualizar}\n Estos son los posts:')
            ObtenerDatosApi()
    elif realizar == '2':
        opcion_crear = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\nIngrese el numero de la opcion: ')
    elif realizar == '3':
        opcion_editar = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\nIngrese el numero de la opcion: ')
    elif realizar == '4':
        opcion_eliminar = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\nIngrese el numero de la opcion: ')
