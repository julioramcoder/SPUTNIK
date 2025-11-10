#adivina el numero
import random   
Numero_aleatorio = random.randint(1, 100)
intentos = 0        
print("¡Bienvenido al juego de adivinar el número!")
while True:
    intento = int(input("Adivina un número entre 1 y 100: "))
    intentos += 1
    if intento < Numero_aleatorio:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > Numero_aleatorio:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número {Numero_aleatorio} en {intentos} intentos.")
        break