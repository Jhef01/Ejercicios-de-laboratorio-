#Suma de Dígitos:
#Pide al usuario un número entero positivo. Calcula la suma de sus dígitos utilizando un bucle
#hile.
n=int(input("ingrese un numero entero positivo "))
suma=0
while n>0:
    suma +=n%10
    n=n//10
print(f"la suma de los numeros digitos es:{suma}")