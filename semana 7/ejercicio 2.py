def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."

def calculadora():
    try:
        # Solicitar dos números al usuario
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        # Solicitar el tipo de operación
        print("Operaciones disponibles: + (suma), - (resta), * (multiplicación), / (división)")
        operacion = input("Ingresa el tipo de operación que deseas realizar: ")

        # Realizar la operación correspondiente
        if operacion == '+':
            resultado = suma(num1, num2)
        elif operacion == '-':
            resultado = resta(num1, num2)
        elif operacion == '*':
            resultado = multiplicacion(num1, num2)
        elif operacion == '/':
            resultado = division(num1, num2)
        else:
            print("Operación no válida. Por favor, ingresa una operación válida.")
            return
        
        print(f"El resultado es: {resultado}")
    
    except ValueError:
        print("Entrada no válida. Por favor, ingresa números.")

# Llamar a la función de la calculadora
calculadora()