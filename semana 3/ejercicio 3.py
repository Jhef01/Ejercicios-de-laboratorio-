
# Solicitar la lista de notas en una sola entrada, separadas por comas
notas= input("Ingrese una lista de notas separadas por comas: ")

# Convertir la entrada en una lista de números
notas = [float(nota) for nota in notas.split(",")]

# Calcular el promedio de las notas
promedio = sum(notas) / len(notas)

# Mostrar el promedio
print(f"El promedio de las notas es: {promedio}")