#Contar Vocales en una Frase:
#pide al usuario una frase y cuenta el número total de vocales (mayúsculas y minúsculas)
#utilizando un bucle for
cadena =input("ingrese una frase")
vocales="aeiouAEIOU"
contador=0
for x in cadena:
    if cadena in vocales:
        contador+=1
print(f"el numero de vocales es{contador}")