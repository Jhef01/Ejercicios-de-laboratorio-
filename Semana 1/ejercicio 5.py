# Solicitar al usuario que introduzca su nombre, apellido, país y edad
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
pais = input("Introduce tu país: ")
edad = input("Introduce tu edad: ")

# Convertir la edad a un tipo numérico (entero)
edad = int(edad)

# Mostrar los datos ingresados
print("Nombre:", nombre)
print("Apellido:", apellido)
print("País:", pais)
print("Edad:", edad)