#sumar hasta que el usuario escriba 0
suma = 0
while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print("La suma total es:", suma)