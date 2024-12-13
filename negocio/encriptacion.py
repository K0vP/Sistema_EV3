from cryptography.fernet import Fernet

def generar_clave():
    return Fernet.generate_key()

def encriptar_contrasena(contrasena, clave):
    fernet = Fernet(clave)
    contrasena_encriptada = fernet.encrypt(contrasena.encode())
    return contrasena_encriptada

def desencriptar_contrasena(contrasena_encriptada, clave):
    fernet = Fernet(clave)
    contrasena_desencriptada = fernet.decrypt(contrasena_encriptada).decode()
    return contrasena_desencriptada