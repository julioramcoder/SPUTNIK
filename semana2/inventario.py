#---------------------------------Task 1------------------------------
"""
1. Validación de datos con condicionales:
Crea un menú que pregunte al usuario qué acción desea realizar:
Agregar producto
Mostrar inventario
Calcular estadísticas
Salir
Usa condicionales if, elif y else para procesar la opción elegida.
Si el usuario ingresa una opción inválida, muestra un mensaje de error y pide nuevamente la entrada."""

print("Bienvenido a inventariofacil.com \nElige una opción: ")

print("1: Agregar producto")
print("2: Mostrar inventario")
print("3: Calcular estadísticas")
print("4: Salir\n")

while True:
    try:
        menu = int(input())
        break
    except ValueError:
        print("Ingresa una opción válida")


#--------------------------Task 2-----------------------------------
"""
2. Implementar un bucle para múltiples registros:
Envuelve el menú en un bucle while que continúe ejecutándose hasta que el usuario elija salir.
Permite agregar varios productos seguidos (nombre, precio y cantidad).
Cada producto debe almacenarse como un diccionario dentro de una lista llamada inventario.
producto = {"nombre": "Lápiz", "precio": 500, "cantidad": 3}
inventario.append(producto)"""

inventario = []

def createNewItem(_nombre,_precio,_cantidad):
    newItem = dict(nombre = _nombre, precio = _precio, cantidad =_cantidad)
    return newItem

def addNewItem(_nombre,_precio,_cantidad):
    inventario.append(createNewItem(_nombre,_precio,_cantidad))

#-----------------Task 3------------------------------------------
"""
Mostrar todos los productos del inventario:
Implementa una opción en el menú que recorra el inventario con un bucle for.
Muestra todos los productos en un formato claro:
Producto: Lápiz | Precio: 500 | Cantidad: 3
Si el inventario está vacío, muestra un mensaje que lo indique."""

def showItems():
    if not inventario:
        print("Aun no hay productos en el inventario")
    else:
        print(f"{'Producto':<25} {'Precio':<10} {'Cantidad':<10}")
        print("-" * 45)
        for item in inventario:
            print(f"{item["nombre"]:<25} {item["precio"]:<10.2f} {item["cantidad"]:<10}")
            

addNewItem("coco",2,4)
addNewItem("cosco",2,4)
addNewItem("co4co",2,4)
addNewItem("coc2o",2,4)
showItems()

#----------------Task 4------------------------------------------
"""
 Calcular estadísticas básicas:
Implementa en el menú una opción para calcular:
El valor total del inventario (sumatoria de precio x cantidad).
La cantidad total de productos registrados.
Muestra los resultados usando print() de manera clara."""

def totalItem(item):
    cantidad = item["cantidad"]
    precio = item["precio"]
    return cantidad*precio

def cantidadTotal():
    total = 0
    for item in inventario:
        total += item["cantidad"]
    print(f"La cantidad total de productos es: ") #aqui tengo que solucionar la ambiguedad de si es productos unitarios, sin repetir, etc
    return total

for item in inventario:
    print(f"el total de {item["nombre"]} es: {totalItem(item)}")

print(cantidadTotal())

#-------------Task 5----------------------------------------------
"""
Documentación y limpieza del código:
Comenta el código explicando la funcionalidad de cada sección (menú, bucle, validación, estadísticas).
Estructura el código en funciones simples:
agregar_producto()
mostrar_inventario()
calcular_estadisticas()
Deja un comentario final resumiendo el objetivo de la semana."""




    