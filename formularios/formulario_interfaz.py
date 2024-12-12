from auxiliares.constantes import visualizar
from servicios.obtener_datos_api import ObtenerDatosApi
from servicios.actualizar_datos_api import ActualizarDatosApi
def menu ():
    print('Bienvenido')
    realizar = input('Que desea realizar:\n1: Consultar\n2: Crear\n3: Editar\n4: Eliminar\n5: salir\nIngrese el numero de la opcion: ')
    if realizar == '1':
        opcion_consultar = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\n3: Volver al menu\nIngrese el numero de la opcion: ')
        if opcion_consultar in visualizar:
            print (f'Selecciono la opcion {visualizar[opcion_consultar]}:\n')
            ObtenerDatosApi(opcion_consultar)
        elif opcion_consultar == "3":
            menu()
    elif realizar == '2':
        opcion_crear = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\nIngrese el numero de la opcion: ')
    elif realizar == '3':
        opcion_editar = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\n3: Volver al menu\nIngrese el numero de la opcion: ')
        if opcion_editar in visualizar:
            print (f'Selecciono la opcion {visualizar[opcion_editar]}')
            IdActualizar = int(input(f"ingrese le id del {visualizar[opcion_editar]} que quiere actualizar:"))
            ActualizarDatosApi(opcion_editar,IdActualizar)
        elif opcion_editar == "3":
            menu()
    elif realizar == '4':
        opcion_eliminar = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\n3: Volver al menu\nIngrese el numero de la opcion: ')
    elif realizar == "5":
        print("¡Hasta Luego!")
