#we are goona to do a inventory platform

print("=============== GOOD HOME COOKING ==============")

#we need to  beging asking to the user basic information usign the command while

name = input("HEY!, it's a pleasure to meet you, Please type your username: ")  
agregar_producto = 1
print(".\n",name,"si quiere agregar un producto nuevo al inventario por favor digita el numero 1.\n")
Mostrar_inventario = 2
print(name,"si quiere revisar lo que tiene en el inventario por favor imgresa el numero 2.\n")
calcular_estadistica = 3
print(name,"si quiere revisar las estaditicas por favor ingrese el nmumero 3.\n")
salir = 4
print ("si quiere salir del programa presione 4.\n")

#actividad = input(name,"Por favor indicame que quieres hacer hoy: ")  

#CREAREMOS UNA LISTA VACIA INMUTABLE FUERA DEL BUCLE PARA QUE SE GUARDE TODOO AQUI 

INVENTARIOS = []

while True:
    actividad = int(input(name+ "Por favor indicame que quieres hacer hoy: "))
    
    if actividad < 1 or actividad > 4:
        print(name + "Lo siento esa opcion no es valida por favor vuelve a ingresar")

    
    
    elif actividad == 1:
        while True:
            Lista_nueva = []
            print(".\nNUEVO INVENTARIO INICIADO.\n")
            
            nombre = input ("por favor ingrese el nombre del nuevo producto: ")
            precio = float(input("por favor ingresa el valor del producto por unidad: "))
            cantidad = int(input("por favor ingrese la cantidad de productos: "))
            
            Lista_nueva.append((nombre,precio,cantidad))
            INVENTARIOS.append(Lista_nueva)
            numero = 1
            for i in INVENTARIOS: 
                for item in i:
                    print (f"inventario{numero} ({item[0]},{item[1]},{item[2]})")
                numero += 1
                
            continuar = input(name + "Quieres continuar con el inventario?(si/no): ").lower()
            
    
            if continuar == "no":
                print(name + "vamos a salir del inventario en este momento")
                break
        
