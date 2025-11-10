#---------------------Task 2---------------------

print("Bienvenido a InventarioFacil.com \ningresa los siguientes datos para agregar un nuevo producto") 

itemName = input("Nombre del producto: ") #itemName almacena el nombre del producto

while  itemName.isdecimal() or itemName.isspace(): #bucle while, solo se entra si itemName conitene solo números o espacios
                                                   #Si se entra en el bucle, se vuelve a pedir al usuario un nombre de producto
                                                   #el bucle se repite hasta que itemName sea correcto
                                                   #si el valor ingresado no es correcto, se explica el error al usuario
    itemName = input(f"{itemName} es inválido. No es posible nombrar productos solo con numeros o espacios \npor favor ingresa un nombre válido: ")

itemPrice = input("Precio del producto: ") #itemPrice almacena el precio del producto

while  not itemPrice.isdecimal():  #si el valor almacenado no es decilmal, se entra al bucle para volver a pedir un nuevo valor
                                                                        
    itemPrice = input(f" {itemPrice} es inválido, por favor ingresa un precio numérico y positivo: ") #si el valor ingresado no es correcto, se explica el error al usuario


itemPrice = float(itemPrice)  #si se sale del bucle, es porque el usuario ingreso un valor correcto, entonces es posible 
                              #convertir itemPrice a tipo flotante

itemCount = input("Cantidad del producto: ") #itemCount almacena el numero de productos

while not itemCount.isdecimal():  #funciana igual que itemPrice
    itemCount = input(f" {itemCount} es inválido, por favor ingresa una cantidad entera y positiva: ") 
itemCount = int(itemCount)

#---------------------Task 3---------------------

costoTotal = itemCount*itemPrice #costoTotal calcula es costo de tener "x" productos a "y" precio con la fórmula x*y
                                 #como ya es seguro que "x" es int y  "y" float, no es necesario comprobar el tipo de costoTotal, será float

#---------------------Task 4---------------------

print(f"Producto: {itemName} | Precio: {itemPrice} | Cantidad: {itemCount} | Total: {costoTotal}") # se muesta al usuario la información de su producto 
                                                                                                   # (nombre, precio, cantidad, costo total)

#---------------------Task 5---------------------

#inventario.py es un programa que permita al usuario ingresar un único producto a un inventario. El programa
#solicita nombre, precio y cantidad del producto, cada una de estas entradas cuenta con un sistema de validación
#una vez todos los datos son válidos, el programa calcula el precio total del inventario y muesta toda la información al usuario.