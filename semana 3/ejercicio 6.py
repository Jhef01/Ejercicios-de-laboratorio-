a=float(input("ingrese un numero"))
b=float(input("ingrese otro numero"))
c=float(input("ingrese el ultimo numero"))
if a>b and b>c:
    print(f"el numero mayor de los 3 ingresados es : {a}")
elif b>a and a>c:
        print(f"el numero mayor es: {b}")
else:
    print(f"el numero mayor de los tres numeros ingresados es: {c}")
