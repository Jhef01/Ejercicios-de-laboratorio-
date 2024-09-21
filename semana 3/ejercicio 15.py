#Número de Teléfono con Formato:
#Pide al usuario un número de teléfono de 10 dígitos y utiliza slicing y concatenación para darle
#el formato "(###) ###-####".
telefono = input("Ingresa tu número de teléfono de 10 dígitos: ")
# Verificamos que el número tenga exactamente 10 dígitos
if len(telefono) == 10 and telefono.isdigit():
    # Aplica el formato
    formateado = "(" + telefono[:3] + ") " + telefono[3:6] + "-" + telefono[6:]
    print("El número con formato es:", formateado)
else:
    print("Número inválido. Asegúrate de ingresar exactamente 10 dígitos.")
