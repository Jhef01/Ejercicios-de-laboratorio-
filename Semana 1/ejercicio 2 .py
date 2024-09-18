n="jheferson"               #nombre
a="Vargas"                  #apellidos
longitud= len(n)==len(a)    #comparacion (==)
print(longitud)             
if longitud:                
    print(f"la longitud del apellido {n} es igual a la longitud del nombre  {a} ")
else:
    print(f"La longitud del nombre {n} y el apellido {a} es diferente.")