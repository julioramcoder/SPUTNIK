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
    itemPrice = float(input("Precio del producto: "))
    itemCantidad = int(input("Cantidad de producto: "))

    addNewItem(itemName, itemPrice, itemCantidad)
    print(f"Agregado producto: {itemName} con un precio de: {itemPrice} y una cantidad de: {itemCantidad}")

def showItems():
    if not inventario:
        print("Aun no hay productos en el inventario")
    else:
        print(f"{'Producto':<25} {'Precio':<10} {'Cantidad':<10}")
        print("-" * 45)
        for item in inventario:
            print(f"{item["nombre"]:<25} {item["precio"]:<10.2f} {item["cantidad"]:<10}")

# funciones de estadística:

def totalItem(item):
    cantidad = item["cantidad"]
    precio = item["precio"]
    return cantidad*precio

def cantidadTotal():
    total = 0
    for item in inventario:
        total += item["cantidad"]
    print(f"La cantidad total de productos es: ") 
    return total

def precioTotal():
    total = 0
    for item in inventario:
        total += totalItem(item)

#-------------------------------------------------------------------------------
# Funciones menu

def agregarProductoMenu():
    agregarProducto()
    while True:
        print("1: Agregar nuevo item: ")
        print("2: Salir: ")
        menu = int(input())

        if menu == 1:
            agregarProducto()
        elif menu == 2:
            print("Volviendo al menu principal"); break
        else: print("opción inválida")

#-------------------------------------------------------------------------------
# Menu




print("Bienvenido a inventariofacil.com \nElige una opción: ")

print("1: Agregar producto")
print("2: Mostrar inventario")
print("3: Calcular estadísticas")
print("4: Salir\n")

while True:
    menu = ""
    try:
        menu = int(input())
        break
    except ValueError:
        print("Ingresa una opción válida")
    
    match menu:
        case 1:
            print("caso 1")
            agregarProductoMenu()


    





            









