#Considera dos listas, l1 y l2, que contienen tuplas. Cada tupla consta de una cadena de texto y
#un número entero. La lista l1 tiene 5 elementos y la lista l2 tiene 3 elementos. (7ptos)
l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]
#Tu tarea es:
#a. Crear conjuntos a partir de estas listas, s1 y s2.
conj_1=set(l1)
conj_2=set(l2)
#b. Encontrar los elementos que son comunes a s1 y s2 y almacenarlos en un conjunto s3.
interseccion=conj_1.intersection(conj_2)
conj_s3=set(interseccion)
print("elementos que son comunes a s1 y s2 y almacenarlos en un conjunto s3 :",conj_s3)
#c. Encontrar los elementos que son únicos para s1 y s2 y almacenarlos en un conjunto s4.
diferencia_1=conj_1.difference(conj_2)
diferencia_2=conj_2.difference(conj_1)
conj_s4=diferencia_1.union(diferencia_2)
print("los elementos que son únicos para s1 y s2 y almacenarlos en un conjunto s4",conj_s4)
#d. Crear una nueva lista l3 que contenga los elementos de s3 y s4 ordenados por el número entero
#de cada tupla.
l3 = list(conj_s3.union(conj_s4))  # Unir los conjuntos s3 y s4 y convertir en lista
n = len(l3)  # Obtener la longitud de la lista
for i in range(n):  # la variable "i" recorrera toda la longitud de la lista l3.
    for j in range(0, n-i-1):  # Recorrer la lista hasta el elemento no ordenado
        if l3[j][1] > l3[j+1][1]:  # Comparar el segundo valor de cada tupla
            l3[j], l3[j+1] = l3[j+1], l3[j]  # Intercambiar si están en el orden incorrecto

print(f"Lista l3 (elementos ordenados por el número entero): {l3}")  #Se Imprimira la lista de forma ordenada.