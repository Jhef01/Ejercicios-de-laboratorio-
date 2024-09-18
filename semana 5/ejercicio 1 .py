# La siguiente es una lista de las edades de 10 estudiantes:
edades=[19,22,19,24,20,25,26,24,25,24]
#a. Ordena la lista y encuentra la edad mínima y máxima
edades.sort()
min=edades[0]
max=edades[-1]
print(f"edad minima es: {min},y la edad maxima es: {max}")
#Añade de nuevo la edad mínima y máxima a la lista
edades.append(min)
edades.append(max)
print(f"la nueva lista edades mas el maximo y el minimo es ={edades}")
#c. Encuentra la edad mediana (un elemento del medio o dos elementos del medio divididos por dos)
n = len(edades)
if n%2==0:
    mediana=((edades[n//2-1])+(edades[n//2]))/2
else :
    mediana=edades[n//2]
print(f"la edadad mediana de la lista es {mediana}")
#d. Encuentra la edad promedio (suma de todos los elementos divididos por su número)
promedio=sum(edades)/n
print(f"el promedio es: {promedio}")
#e. Encuentra el rango de las edades (máximo menos mínimo)
Rango=max-min
print(f"el rango de las edades es :{Rango}")
#f. Compara el valor de (mínimo - promedio) y (máximo - promedio), usa el método abs()
dif_min=abs(min-promedio)
dif_max=abs(max-promedio)
if dif_min>dif_max:
    print(f"la diferencia (minima-promedio) es mayor porque vale :{dif_min}")
elif dif_max>dif_min:
    print(f"la diferencia (maxima-promedio) es mayor porque vale :{dif_max}")
else :
    print("las diferencias son iguales")




