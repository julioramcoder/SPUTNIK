#Tabla de multiplicar.

numero = int(input("¿De qué número quieres la tabla?: "))                 #se pide al usuario el numero
limite = int(input(f"¿Hasta qué número quieres la tabla del {numero}? ")) #se pide al usuario el límite

for i in range(1,limite + 1):                                             #bucle for que termine cuando i = limite
    print(f"{numero} x {i} = {numero*i}")                                 #se muestra al usuario el resultado de numero * i