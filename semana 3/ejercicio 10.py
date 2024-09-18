print("Bienvenido al conversor de unidades")
longitud=float(input("ingrese una longitud en metros: "))
convertir=input("ingrese la unidad a la que desea convertir (pies,pulgadas,yardas): ").lower()
if convertir=="pies":
    rpta=longitud*3.28
    print(f"la longitud convertida en pies es : {rpta}")
elif convertir=="pulgadas":
    rpta=longitud*39.37
    print(f"la longitud convertida en pulgadas es: {rpta}")
elif convertir=="yardas":
    rpta=longitud*1.09361
    print(f"la longitud convertida en yardas es:{rpta}")
else:
    print("EROR ,ingrese una de las unidades escritas al incio")

