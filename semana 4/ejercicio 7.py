#Invertir una Cadena:
#Pide al usuario una cadena e inviértela utilizando un bucle for
cdn=input("ingrese una cadena ")
cadena_invertida =""
for letra in cdn:
    cadena_invertida = letra + cadena_invertida
print(cadena_invertida)