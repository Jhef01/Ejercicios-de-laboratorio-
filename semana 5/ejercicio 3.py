#Considera tres listas de números enteros, una con números del 1 al 10, otra con números del 5 al
#15, y la última con números del 10 al 20. (5ptos)
num_1_10=[1,2,3,4,5,6,7,8,9,10]
num_5_20=[5,6,7,8,9,10,11,12,13,14,15]
num_10_20=[10,11,12,13,14,15,16,17,18,19,20]
#a. Convierte las listas en conjuntos.
conj_1=set(num_1_10)
conj_2=set(num_5_20)
conj_3=set(num_10_20)
#b. Encuentra el conjunto de todos los números que están presentes en las tres listas.
interseccion=conj_1.intersection(conj_2,conj_3)
print("la interseccion es: ",interseccion)
#c.Encuentra el conjunto de todos los números que están presentes en al menos una de las lista.
union=conj_1.union(conj_2,conj_3)
print("la union es:",union)
#d. Encuentra el conjunto de todos los números que están presentes en la primera lista, pero no en
#la última.
diferencia=conj_1.difference(conj_3)
print("la diferencia es: ",diferencia)
#e. Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla.
tpl_1=tuple(interseccion)
tpl_2=tuple(union)
tpl_3=tuple(diferencia)
sum_interseccion=tpl_1[0]+tpl_1[-1]
sum_union=tpl_2[0]+tpl_2[-1]
sum_diferencia=tpl_3[0]+tpl_3[-1]
print("la suma del primer y último elemento de cada tupla son : ",sum_interseccion,sum_union,sum_diferencia)