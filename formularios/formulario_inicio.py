def iniciar_sesion():
    from modelos.usuario import usuario
    from datos.conect_db import config
    from negocio.encriptacion import desencriptar_contrasena, encriptar_contrasena, generar_clave
    import getpass

    
    print('--------------------------------------------\n|Bienvenido al sistema de EcoTech Solutions|\n--------------------------------------------\n\nIngrese sus credenciales: \n')

    rut = input('Rut (con guion y digito verificador): ')
    query = "SELECT contrasena_encriptada, nombre_estado FROM empleados emp INNER JOIN estado est ON emp.estado = est.id_estado WHERE rut = %s;"
    resultado = config(query, rut)
    
    if resultado:
        contrasena_encriptada = resultado[0][0]
        estado = resultado[0][1].strip().lower()
        
        if estado == 'activo':
            contrasena = getpass.getpass("Introduce tu contraseña: ")
            clave = generar_clave()
            contrasena_encriptada = encriptar_contrasena(contrasena, clave)
            contrasena_desencriptada = desencriptar_contrasena(contrasena_encriptada, clave)
            
            if contrasena == contrasena_desencriptada:
                print('\nBienvenido')
                usuario(rut)
                return
            else:
                print("Contraseña incorrecta.")
        elif estado == "deshabilitado": 
            print('Cuenta deshabilitada. ¡Actualice el estado, si se utilizara la cuenta!')
        else:
            print("¡Hasta luego!")
    else:
        print("Usuario no encontrado.")