#pedir 2  numeros al usuario y una operacion matematicas 
#suma
#resta (el primero - segundo)
#devision (el primero/segundo)
#exponensiciones
#radicacion 

#definimos la funcion primera mente y los argumentos que es la informacion que necesitamos

def suma (n1,n2):
    sumas = n1 + n2
    return sumas

def resta (n1,n2):
    restas = n1 - n2
    return restas

def division(n1,n2):
    divisiones = n1/n2
    return divisiones

def exponen (n1,n2):
    exponens = n1**n2
    return exponen
def radicales(n1,n2):
    radic = n1 ** (1/n2)
    return radic
   
  
print(" ========== A continuacion te daremos las operaciones matematicas que podras ejecutar ==========\n")
print("1. Suma\n")
print("2. Resta (el primer num - el segundo num)\n")
print("3. Division (el primer num/el segundo num)\n")
print("4. Exsposiciones\n")
print("5. Radicacion\n")

while True:     

    opera= float(input("\nPor favor selecciona uno de los valores que te mostramos anteriormente para ajecutarlo:\n"))
    
    if opera < 1 or opera > 5:
        print("\n====ERROR, LO SIENTO, PERO EL VALOR INDICADO NO CORRESPONDE, INTENTA DE NUEVO====\n")
    
    elif opera == 1:
        n1=float(input("Ingrese el primer numero: \n"))
        n2=float(input("Ingrese el segundo numero"))
        print(f"El resultado de la suma es: {suma(n1,n2)}:\n ")
        
    elif opera == 2:
        n1=float(input("\nIngrese el primer numero: "))
        n2=float(input("\nIngrese el segundo numero: "))
        print(f"\nEl resultado de tu resta es: {resta(n1,n2)}: ")
        
    elif opera == 3:
        n1=float(input("\nIngrese el primer numero: "))
        n2=float(input("\nIngrese el segundo numero: "))
        print(f"\nEl resultado de tu division es: {division(n1,n2)}: ")
        
    elif opera == 4:
        n1=float(input("\nIngrese el primer numero: "))
        n2=float(input("\nIngrese el segundo numero: "))
        print(f"\nEl resultado de tu exponensiacion es: {exponen(n1,n2)}: ")
    
    elif opera == 5:
        n1=float(input("\nIngrese el primer numero: "))
        n2=float(input("\nIngrese el segundo numero: "))
        print(f"\nEl resultado es{radicales(n1,n2)}: ")
    break
    
    