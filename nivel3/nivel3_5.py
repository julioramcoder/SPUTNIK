#Adivina el número (usar random)

import random                                 # importa la librería random para poder usar randint

numero = random.randint(1,1000)               # randint(a,b) da un entero random entre a y b //no estoy seguro de si incluye a y b, tengo que buscar luego

print("estoy pensando un número del 1 al 1000 \n¿puedes adivinarlo?")    #se indica al usuario lo que debe hacer

while True:                                    # bucle while que siempre es True, se va a ejecutar hasta llegar a algún break
    guess = int(input("Número: "))             #pide al usuario la adivinanza

    if guess == numero: print(f"¡¡Lo lograste!! el número es: {guess}" ); break #si la adivinanza coincide con numero, felizita al usuario y sale del bucle

    elif guess < numero: print(f"{guess} es demasiado pequeño")     #si no es igual, le da una pista dependiendo de si se pasó o no llegó al numero

    else: print(f"{guess} es demasiado grande")