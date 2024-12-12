def iniciar_sesion():
    from modelos.empleados import Empleados
    from datos.consultas_db import DB_consulta_validar
    import getpass

    print('--------------------------------------------\n|Bienvenido al sistema de EcoTech Solutions|\n--------------------------------------------\n\nIngrese sus credenciales: \n')

    rut = input('Rut (con guion y digito verificador): ')
    query = "SELECT nombre_estado FROM empleados emp INNER JOIN estado est ON emp.estado = est.id_estado WHERE rut = %s;"
    resultado = DB_consulta_validar(query,rut)
    estado = resultado[0][0].strip().lower() if resultado else None
    if estado == 'activo':
        contrasena = getpass.getpass("Introduce tu contraseña: ")
        if Empleados.validarDatos(rut,contrasena):
            print('\nBienvenido')
            interfaz(rut)
            return
    elif estado == "deshabilitado": 
        print('Cuenta deshabilitada. ¡Actualice el estado, si se utilizara la cuenta!')
    else:
        print("¡Hasta luego!")