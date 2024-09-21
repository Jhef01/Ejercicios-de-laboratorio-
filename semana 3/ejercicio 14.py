#Piedra, Papel o Tijera:
#Pide al usuario que elija "piedra", "papel" o "tijera". Genera una elección aleatoria para la
#computadora y determina quién gana.
import random  
print("Bienvenido al juego de piedra,papel o tijera")
opciones = ["piedra", "papel", "tijera"]
usuario = input("Elige piedra, papel o tijera: ").lower()
if usuario not in opciones:
    print("Opción no válida. Por favor elige 'piedra', 'papel' o 'tijera'.")
else:
    # Genera una elección aleatoria para la computadora
    computadora = random.choice(opciones)
    # Muestra la elección de la computadora
    print("La computadora eligió:", computadora)
    # Determina el resultado del juego
    if usuario == computadora:
        print("Es un empate.")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste.")