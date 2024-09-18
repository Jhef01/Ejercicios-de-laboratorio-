# Número de filas y columnas en la tabla
num_filas = 4
num_columnas = 4

# Imprimir la tabla
for i in range(1,num_filas + 1):
    for j in range(num_columnas):
        # Calcula el valor a mostrar
        valor = i ** j
        # Imprime el valor en formato de tabla, con un espacio para separación
        print(valor, end=' ')
    # Imprime una nueva línea al final de cada fila
    print()
