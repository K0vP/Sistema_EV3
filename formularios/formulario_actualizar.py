def FormActulizar(opcion):
    if opcion == "1":
            dato = {
                "tittle": "",
                "body": ""
                }
            dato["tittle"] = input("Ingrese el titulo nuevo del post:")
            dato["body"] = input("Ingrese el contenido nuevo del post:")
            return dato
    elif opcion == "2":
            dato = {
                "name": "",
                "email": "",
                "body": "",
                }
            dato["name"] = input("Ingrese el nombre nuevo:")
            dato["email"] = input("Ingrese el correo nuevo:")
            dato["body"] = input("Ingrese el contenido nuevo:")
            return dato