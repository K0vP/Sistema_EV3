from auxiliares.constantes import visualizar
from negocio.negocio_manejo_datos import Datos
from servicios.obtener_datos_api import ObtenerDatosApi
from servicios.actualizar_datos_api import ActualizarDatosApi
from datos.iniciar_db import iniciar_db
from modelos.posts import Post
from modelos.comments import Comment
from servicios.crear_datos_api import CrearPostApi, CrearCommentApi
from negocio.encriptacion import generar_clave, encriptar_contrasena, desencriptar_contrasena
from servicios.consulta_api import buscar_en_serper
import json
def menu ():
    print('Bienvenido')
    iniciar_db()
    realizar = input('Que desea realizar:\n0: Cargar datos a la bd\n1: Consultar\n2: Crear\n3: Editar\n4: Eliminar\n5: encriptar contrasena\n6: Consulta api\n7: salir\nIngrese el numero de la opcion: ')
    if realizar == '0':
        opcion_subir_datos = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\n3: Volver al menu\nIngrese el numero de la opcion: ')
        if opcion_subir_datos in visualizar:
            print (f'Selecciono la opcion {visualizar[opcion_subir_datos]}:\n')
            Datos(opcion_subir_datos)
    elif realizar == '1':
        opcion_consultar = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\n3: Volver al menu\nIngrese el numero de la opcion: ')
        if opcion_consultar in visualizar:
            print (f'Selecciono la opcion {visualizar[opcion_consultar]}:\n')
            ObtenerDatosApi(opcion_consultar)
        elif opcion_consultar == "3":
            menu()
            
    elif realizar == '2':
        opcion_crear = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\n3: Volver al menu\nIngrese el numero de la opcion: ')
        if opcion_crear == '1':
            user_id = input('Ingresar el id del usuario: ')
            title = input('ingresar el titulo del post: ')
            body = input('ingresar el cuerpo del post: ')
            post = Post(user_id, None, title, body)
            CrearPostApi(post)
        elif opcion_crear == '2':
            post_id = input('ingresar el id del post: ')
            name = input('Ingrese el nombre del autor del comment: ')
            email = input('Ingrese el email del autor del comment: ')
            body = input('ingresar el cuerpo del comment: ')
            comment = Comment(post_id, id, name, email, body)
            CrearCommentApi(comment)
        elif opcion_crear == '3':
            menu()
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
       
    elif realizar == '5':
        clave = generar_clave()
        contrasena = input('Ingrese la contraseña a encriptar: ')
        print(f'Contraseña ingresada: {contrasena}')
        
        contrasena_encriptada = encriptar_contrasena(contrasena, clave)
        print(f'Contraseña encriptada: {contrasena_encriptada}')
        
        print("Desencriptando la contraseña para comparar...")
        contrasena_desencriptada = desencriptar_contrasena(contrasena_encriptada, clave)
        
        print(f'Comparando contraseñas: \nOriginal: {contrasena} \nDesencriptada: {contrasena_desencriptada}')
        if contrasena == contrasena_desencriptada:
            print('La contraseña ha sido desencriptada correctamente y coincide con la original.')
        else:
            print('Error: La contraseña desencriptada no coincide con la original.')

    elif realizar == '6':
        query = input("Ingrese el string de búsqueda: ")  # Solicitar el string de búsqueda al usuario

        resultados = buscar_en_serper(query)  # Realizar la búsqueda

        if resultados:
            print("Resultados de la búsqueda:")
            print(json.dumps(resultados, indent=4))  # Imprimir los resultados de forma legible
            
    elif realizar == "7":
        print("¡Hasta Luego!")
