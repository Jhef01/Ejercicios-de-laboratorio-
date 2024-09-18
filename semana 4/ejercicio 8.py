#Número de Fibonacci:
#Pide al usuario un número entero positivo 'n'. Calcula el enésimo número de Fibonacci
#utilizando un bucle for
n=int(input("ingrese un numero entero positivo "))
a,b=0,1
for i in range(n):
    print(a," ")
    a,b=b,a+b