precio=float(input("ingrese el precio original del producto: "))
categoria_descuento=input("introduce la categoria de descuento (estudiante,jubilado,empleado,otro): ").lower()
if categoria_descuento == "estudiante" :
   dsc=precio*(10/100)
   rpta=precio-dsc
   print(f"el descuento del precio si eres estudiante es:{rpta}")
elif categoria_descuento=="jubilado":
   dsc=precio*(15/100)
   rpta=precio-dsc
   print(f"el descuento si eres jubilado es: {dsc}")
elif categoria_descuento=="empleado":
   dsc=precio*(5/100)
   rpta=precio-dsc
   print(f"el descuento si eres empleado es:{rpta} ")
else :
   print(f"el descuento para otros es: {precio}")
   
