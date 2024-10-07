import random #este modulo permite seleccionar de modo aleatorio los caracteres para formar la contraseña.
import string #usamos este modulo porque tiene varios caracteres que necitaremos para hacer el codigo .
def generar_contrasena(longitud):
    while True:
        caracteres = string.ascii_letters+ string.digits+string.punctuation  # Conjunto de caracteres disponibles (letras, dígitos y símbolos)
        contrasena=" ".join(random.choice(caracteres) for i in range(longitud))  # Generar contraseña aleatoria sin espacios
        # Verificar si la contraseña cumple con todos los requisitos
        if (any(c.isupper() for c in contrasena) and # Al menos una mayúscula
            any(c.islower() for c in contrasena) and # Al menos una minúscul
            any(c.isdigit() for c in contrasena) and # Al menos un número
            any(c in string.punctuation for c in contrasena)): # Al menos un símbolo
            return contrasena
#programa principal 
if __name__=="__main__":
    longitud_deseada=int(input("Ingrese la longitud deseada de la contraseña: "))
    if longitud_deseada < 8: #validar si la contraseña es mayor que igual que 8
        print("La contraseña debe tener al menos & caracteres.")
    else:
        contrasena_generada= generar_contrasena(longitud_deseada)
        print("Contraseña generada", contrasena_generada)
