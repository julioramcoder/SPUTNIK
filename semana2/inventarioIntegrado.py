#---------------------------------------------------------------------------
#-----inventarioIntegrado.py------------------------------------------------
#Aqui voy a integrar las 5 task, para darle una mejor estructura al programa

#---------------------------------------------------------------------------

inventario = []

#---------------------------------------------------------------------------
# Funciones para crear diccionario (items) y agregarlos a la lista (inventario)

def createNewItem(_nombre,_precio,_cantidad):
    newItem = dict(nombre = _nombre, precio = _precio, cantidad =_cantidad)
    return newItem

def addNewItem(_nombre,_precio,_cantidad):
    inventario.append(createNewItem(_nombre,_precio,_cantidad))

#---------------------------------------------------------------------------
#  Funciones auxiliares del menu


def agregarProducto():
    itemName = input("Nombre del producto: ")
    while True:
        try:
            itemPrice = float(input("Precio del producto: "))
            itemPrice = abs(itemPrice)
            break
        except ValueError:
            print("el precio debe ser un valor numérico")

    while True:
        try:
            itemCantidad = int(input("Cantidad de producto: "))
            itemCantidad = abs(itemCantidad)
            break
        except ValueError:
            print("la cantidad debe ser un número")

    addNewItem(itemName, itemPrice, itemCantidad)
    print(f"Agregado producto: {itemName} con un precio de: {itemPrice} y una cantidad de: {itemCantidad}")



# funciones de estadística:

def totalItem(item):
    cantidad = item["cantidad"]
    precio = item["precio"]
    return cantidad*precio

def cantidadTotal():
    total = 0
    for item in inventario:
        total += item["cantidad"]
    print(f"La cantidad total de productos es: {total}\n") 
    return total

def precioTotal():
    total = 0
    for item in inventario:
        total += totalItem(item)
    print(f"El precio total del inventario es: {total}\n")

#-------------------------------------------------------------------------------
# Funciones menu

def agregarProductoMenu():
    agregarProducto()
    print("--------------------------------------------------------\n")
    while True:
        print("1: Agregar nuevo item: ")
        print("2: Salir: ")
        menu = int(input())

        if menu == 1:
            agregarProducto()
            print("--------------------------------------------------------\n")
        elif menu == 2:
            print("Volviendo al menu principal")
            showMenu()
            break
        else: print("opción inválida")
        print("--------------------------------------------------------\n")


def showItems():
    if not inventario:
        print("Aun no hay productos en el inventario")
    else:
        print(f"{'Producto':<25} {'Precio':<10} {'Cantidad':<10}")
        print("-" * 45)
        for item in inventario:
            print(f"{item["nombre"]:<25} {item["precio"]:<10.2f} {item["cantidad"]:<10}")
    print("-----------------------------------------------------------------------\n")
    showMenu()

def estadisticas():
    while True:
        print("1: cantidad total de inventario: ")
        print("2: costo total de inventario: ")
        print("3: salir")
        try:
            menuE= int(input())
        except ValueError:
            menuE = 5
            continue

        match menuE:
            case 1:
                cantidadTotal()
            case 2:
                precioTotal()
            case 3:
                print("volviendo al menu principal")
                showMenu()
                break
            case _: print("opción inválida")

#-------------------------------------------------------------------------------
# Menu



def showMenu():

    print("Bienvenido a inventariofacil.com \nElige una opción: ")

    print("1: Agregar producto")
    print("2: Mostrar inventario")
    print("3: Calcular estadísticas")
    print("4: Salir\n")

showMenu()

while True:
    
    try:
        menu = int(input())
        
    except ValueError:
        print("Ingresa una opción válida")
        continue
        
    match menu:
        case 1:
            print("Agregar nuevo producto: \n")
            agregarProductoMenu()
            
        case 2:
            print("Mostrar inventario\n")
            showItems()
        case 3:
            print("Calcular estadísticas\n")
            estadisticas()
        case 4:
            print("saliendo");break
        case _:
            print("Opción inválida\n")


    
            









