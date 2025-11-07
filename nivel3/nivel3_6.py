#Sumar hasta que el usuario escriba 0.

suma = 0   # en suma se almacena el resultado de las futuras adiciones
print("suma todos los números que quieras, pero cuando ingreses 0, la suma terminará ")  # se explica al usuario las instrucciones
while True:         #bucle while siempre True, solo termina cuando llegue a un break
    numero = float(input("siguiente número: ")) #se pide al usuario un numero, puede ser flotante
    if numero == 0: print(f"suma terminada, total: {suma}"); break #si el numero ingresado es 0, muestra la suma y termina el ciclo
    suma += numero                                 #sino, se hace la suma
    print(f"suma actual: {suma}")                  #se muestra en lo que va la suma