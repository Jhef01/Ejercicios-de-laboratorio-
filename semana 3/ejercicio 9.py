año=int(input("ingrese un año del calendario cualquiera : "))
if año % 4==0 :
   print(f"el año {año} es bisiesto")
elif año % 100==0:
   print(f"el año {año} no es bisiesto")
elif año% 400==0:
   print(f"el año {año} es bisiesto")
else :
   print(f"el año {año} no es bisieto")