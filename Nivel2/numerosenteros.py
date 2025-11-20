#numero positivo, negativo o 0
while True:
 entrada = (input("Ingresa un numero, te dire que tipo de numero entero esta clasificado: "))
 
 if entrada.lower() == "salir":
    print("HASTA LUEGO")
    break
 try:     
    numero = float(entrada)
 
    if numero == 0:
        print("Tu numero es Cero 0")
    elif numero >= 1:
        print("Tu numero es positivo")  
    else:
        print("Tu numero es negativo")    

 except ValueError:
     print("no es un numero valido")  
