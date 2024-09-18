# Solicitar la cadena al usuario
cadena = input("Introduce una cadena: ")

# Convertir la cadena a minúsculas y eliminar los espacios para una comparación más precisa
cadena_limpia = cadena.replace(" ", "").lower()

# Verificar si es un palíndromo
if cadena_limpia == cadena_limpia[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
