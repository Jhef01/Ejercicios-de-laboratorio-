# Solicitar los dos números al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
operacion = input("Elija una operación (suma, resta, multiplicación, división): ").lower()
if operacion == "suma":
    s = a + b
    print(f"La suma de los dos números es: {s}")
elif operacion == "resta":
    r = a - b
    print(f"La resta de los dos números es: {r}")
elif operacion == "multiplicación":
    m = a * b
    print(f"La multiplicación de los dos números es: {m}")
elif operacion == "división":
    if b != 0:
        d = a / b
        print(f"La división de los dos números es: {d}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida. Por favor, elija entre suma, resta, multiplicación o división.")
