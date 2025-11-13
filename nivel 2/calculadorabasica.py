# calculadora sencilla con +,-,*,/

numero1 = float(input("ingrese numero 1"))
numero2 = float(input("ingrese numero 2"))

print("cual es la operacion que quieres realizar con los numeros que ingresaste?")

operando = int(input("1. suma /n2. resta /n3 multiplicacion /n4 division / n " ))

match operando: # swicht match/ con 4 casos que funciona con el caso que concida con el valor de la variable operando 25
    case 1:
        print(f"el resultado de {numero1} + {numero2} es: {numero1 + numero2}")
    case 2:
        print(f"el resultado de  {numero1} - {numero2} es: {numero1 - numero2}") 
    case 3:
        print(f"el resultado de {numero1} * {numero2} es: {numero1 * numero2} ")
    case 4:
        print(f"el resultado de {numero1} / {numero2} es: {numero1 / numero2}")
    case  _: 
        print("operacion invalida") 
    
    