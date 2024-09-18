# Solicitar al usuario que ingrese una cadena
cadena_usuario = input("Introduce una cadena: ")

vocales = "aeiouAEIOU"
contador = 0

for caracter in cadena_usuario:
    if caracter in vocales:
        contador += 1

# Mostrar el resultado
print(f"El número de vocales es: {contador}")