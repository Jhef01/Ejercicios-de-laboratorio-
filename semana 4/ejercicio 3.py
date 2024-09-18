#Tabla de Multiplicar con for:
#Pide al usuario un número entero positivo. Imprime la tabla de multiplicar de ese número
#utilizando un bucle for.
n=int(input("ingrese un numero positivo "))
i=0
for i in range(12):
    i=i+1
    m=n*i
    print(f"{n}x{i}={m}")   

    