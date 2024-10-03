import random
import string
# Función para generar una contraseña usando funciones lambda
def generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales):
    caracteres = ''
    agregar_mayusculas = lambda: string.ascii_uppercase if incluir_mayusculas else ''
    agregar_minusculas = lambda: string.ascii_lowercase if incluir_minusculas else ''
    agregar_numeros = lambda: string.digits if incluir_numeros else ''
    agregar_especiales = lambda: string.punctuation if incluir_especiales else ''
    caracteres += agregar_mayusculas()
    caracteres += agregar_minusculas()
    caracteres += agregar_numeros()
    caracteres += agregar_especiales()
    if caracteres == '':
        raise ValueError("Debes seleccionar al menos un tipo de carácter.")
    while True:
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        if (any(c.isupper() for c in contrasena) or not incluir_mayusculas) and \
           (any(c.islower() for c in contrasena) or not incluir_minusculas) and \
           (any(c.isdigit() for c in contrasena) or not incluir_numeros) and \
           (any(c in string.punctuation for c in contrasena) or not incluir_especiales):
            return contrasena
if __name__ == "__main__":
    try:
        longitud_deseada = int(input("Ingrese la longitud deseada de la contraseña: "))
        if longitud_deseada < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
        else:
            incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
            incluir_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
            incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
            incluir_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'
            contrasena_generada = generar_contrasena(longitud_deseada, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales)
            print("Contraseña generada:", contrasena_generada)
    except ValueError:
        print("Entrada no válida. Debes ingresar un número para la longitud.")