from auxiliares.constantes import visualizar
from servicios.obtener_datos_api import ObtenerDatosApi
from modelos.posts import Post
from modelos.comments import Comment
from servicios.crear_datos_api import CrearPostApi, CrearCommentApi
from negocio.encriptacion import generar_clave, encriptar_contrasena, desencriptar_contrasena

def menu ():
    print('Bienvenido')
    realizar = input('Que desea relaizar:\n1: Consultar\n2: Crear\n3: Editar\n4: Eliminar\nIngrese el numero de la opcion: ')
    if realizar == '1':
        opcion_consultar = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\nIngrese el numero de la opcion: ')
        if opcion_consultar in visualizar:
            print (f'Selecciono la opcion {visualizar[opcion_consultar]}:\n')
            ObtenerDatosApi(opcion_consultar)
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
        opcion_editar = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\nIngrese el numero de la opcion: ')
    elif realizar == '4':
        opcion_eliminar = input('Seleccione una de las siguintes opciones:\n1: Post\n2: Comments\nIngrese el numero de la opcion: ')
        
    elif realizar == '5':
        clave = generar_clave()
        contrasena = input('Ingrese la contraseña a encriptar: ')
        print(f'Contraseña ingresada: {contrasena}')
        
        contrasena_encriptada = encriptar_contrasena(contrasena, clave)
        print(f'Contraseña encriptada: {contrasena_encriptada}')
        
        contrasena_desencriptada = desencriptar_contrasena(contrasena_encriptada, clave)
        if contrasena == contrasena_desencriptada:
            print('La contraseña ha sido desencriptada correctamente y coincide con la original.')
        else:
            print('Error: La contraseña desencriptada no coincide con la original.')