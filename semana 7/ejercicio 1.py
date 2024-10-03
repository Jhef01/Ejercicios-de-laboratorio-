#Conversor de Temperatura: Escribe un programa que convierta entre Celsius y Fahrenheit. El
#programa debe permitir al usuario ingresar una temperatura y la unidad en la que está (C o F). Luego,
#realiza la conversión y muestra el resultado. Utiliza funciones y control de flujo para realizar las
#conversiones y manejar excepciones en caso de entradas incorrectas.
def celsius_a_fahrenheit(celsius):
    caf=(celsius * 9/5) + 32
    return caf

def fahrenheit_a_celsius(fahrenheit):
    fac=(fahrenheit - 32) * 5/9
    return fac
def conversor_temperatura():
    try:
        temperatura = float(input("Ingresa la temperatura: "))
        unidad = input("Ingresa la unidad de temperatura (C para Celsius, F para Fahrenheit): ").upper()
        if unidad == 'C':
            resultado = celsius_a_fahrenheit(temperatura)
            print(f"{temperatura}°C son {resultado}°F.")
        elif unidad == 'F':
            # Convertir de Fahrenheit a Celsius
            resultado = fahrenheit_a_celsius(temperatura)
            print(f"{temperatura}°F son {resultado}°C.")
        else:
            print("Unidad no válida. Por favor, ingresa 'C' para Celsius o 'F' para Fahrenheit.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número para la temperatura.")
# Llamar a la función del conversor
conversor_temperatura()