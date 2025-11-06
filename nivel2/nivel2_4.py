#Calculadora básica con +, -, *, /

numero1 = float(input("ingresa el número 1: ")) #se pide el primer número
numero2 = float(input("ingresa el número 2: ")) #se pide el segundo número

print("¿Cúal operación quieres realizar entre los dos números que ingresaste?") #pregunta por la operación

operando = int(input("1. suma \n2. resta \n3 multiplicación \n4 división \n " )) #variable operando almacena la operación (representada con un número según la operación)

match operando:  #switch /match con 4 casos, se ejecuta el caso que coincida con el valor de la variable operando
        case 1:
            print( f"el resultado de {numero1} + {numero2} es: {numero1 + numero2}")
        case 2:
            print( f"el resultado de {numero1} - {numero2} es: {numero1 - numero2}")
        case 3:
            print( f"el resultado de {numero1} * {numero2} es: {numero1 * numero2}")
        case 4:
            print( f"el resultado de {numero1} / {numero2} es: {numero1 / numero2}")
        case _:
            print("operación inválida") #si operando es diferente a 1,2,3,4. No se eligió ninguna operación, se alerta al usuario el error.

