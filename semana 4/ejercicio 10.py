#Calculadora de Promedio:
#Pide al usuario una serie de números separados por comas. Calcula el promedio de esos
#números utilizando un bucle for
serie=input("ingrese una serie de numeros separado por comas")
lista=serie.split(",")
suma=0
for i in serie.split(","):
    suma= suma + float(i)
    promedio=suma/len(lista)
print(f"el promedio de la lista es: {promedio} ")