#Sebastián Álvarez y Shakira Contreras, UJAP. Seguridad en Redes
from cryptography.fernet import Fernet

def generar_llave():
    """
    Función para generar la llave y guardarla en un archivo de extensión .key
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def cargar_llave():
    """
    Carga la llave generada previamente
    """
    return open("secret.key", "rb").read()

def encriptar_mensaje(mensaje):
    """
    Encripta un mensaje
    """
    key = cargar_llave()
    encoded_message = mensaje.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)


    return(encrypted_message)

def decrypt_message(encrypted_message):
    """
    Desencripta un mensaje
    """
    key = cargar_llave()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    print(decrypted_message.decode())


if __name__ == "__main__":
    #Bienvenida
    print("\nBienvenido al programa de criptográficos con clave pública. ")
    print("Se generará su llave pública en el archivo secret.key. . .")
    generar_llave()
    print("¡Llave generada! \n")
    cargar_llave()
    mensaje = input("Ingrese el mensaje a encriptar: ")
    print("\nSu mensaje encriptado es: ")
    encriptado = encriptar_mensaje(mensaje)
    print(encriptado)
    print("¿Desea desencriptar su mensaje?")
    print("1. Si")
    print("2. No")
    while True:
        try:
            eleccion = int(input("Ingrese su opción: "))
            if (eleccion == 1):
                print("\nSu mensaje desencriptado es: ")
                decrypt_message(encriptado)
                break
            elif (eleccion == 2):
                print("Fin del programa.")
                break
            else:
                print("Debe tomar una opción válida")
        except ValueError:
            print("El valor a ingresar debe ser numérico")
        
