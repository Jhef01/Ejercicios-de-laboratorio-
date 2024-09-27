import random
import string
def generar_contrasena(longitud):
    while True:
        caracteres = string.ascii_letters+ string.digits+string.punctuation 
        contrasena=" ".join(random.choice(caracteres) for i in range(longitud))
        if (any(c.isupper() for c in contrasena) and 
            any(c.islower() for c in contrasena) and 
            any(c.isdigit() for c in contrasena) and 
            any(c in string.punctuation for c in contrasena)): 
            return contrasena
if __name__=="__main__":
    longitud_deseada=int(input("Ingrese la longitud deseada de la contraseña: "))
    if longitud_deseada < 8:
        print("La contraseña debe tener al menos & caracteres.")
    else:
        contrasena_generada= generar_contrasena(longitud_deseada)
        print("Contraseña generada", contrasena_generada)