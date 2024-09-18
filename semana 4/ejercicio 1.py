#1) Suma de Números Pares:
#Pide al usuario un número entero positivo 'n'. Calcula la suma de todos los números pares desde
#2 hasta 'n' (inclusive) utilizando un bucle while.

n=int(input("ingrese un número entero positivo"))
suma=0
i=2
while i<=n: 
    suma=suma+i
    i+=2
print(f"la suma de todos los pares es {suma}")