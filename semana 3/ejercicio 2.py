a=input("ingrese la longitud numero 1 para el tirangulo ")
b=input("ingrese la longitud numero 2 para el triangulo ")
c=input("ingrese la longitud numero 3 para el trinagulo ")
if a!=b and a!=c:
    print("el triangulo es escaleno")
elif a==b or b==c:
    print("el triangulo es isosceles")
else :
    print("el triangulo es equilatero")