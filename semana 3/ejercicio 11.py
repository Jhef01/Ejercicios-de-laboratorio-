print("Bienvenido a la calcularadora del indice de masa corporal")
peso = float(input("Ingrese su peso: "))
altura=float(input("ingrese su altura: "))
imc=peso/altura**2
if imc<18.5:
    print("Usted esta Bajo de Peso ")
elif imc>18.5 and imc<24.9: 
    print("Usted tiene peso normal")
elif imc>25 and imc<29.9:
    print("Usted presenta sobrepeso")
else :
    print("usted presenta obesidad")