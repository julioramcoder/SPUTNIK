# Historia de Usuario
#Inventario de Productos

#lista para almacenar los productos
ListaProductos = [] 
print("Hola, Bienvenido al Inventario de Productos")

# Función para agregar un nuevo producto
def agregar_producto():

    print("Agregar un nuevo Producto")
#Solicitar nombre, precio y cantidad del producto al usuario
    nombre = input("Ingrese el nombre del producto: ")
     
    while True:
        try:
        
           precio = float(input("Ingrese el precio del producto: "))

           break
        except ValueError:
           print("Precio inválido. Por favor, ingrese un número válido.")
    while True:
        try:
        
           cantidad = int(input("Ingrese la cantidad del producto: "))

           break
        except ValueError:
           print("Cantidad inválida. Por favor, ingrese un número entero válido.")
# Crear un diccionario para el producto
    inventario = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    ListaProductos.append(inventario) 

    print(f"Producto {nombre} agregado exitosamente.")    
       
# Función para mostrar todos los productos
def mostrar_inventario():
   print("Inventario de Productos:")
   if not ListaProductos:
       print("El inventario está vacío.")   
       return
   for inventario in ListaProductos:
       print(f"  | Nombre: {inventario['nombre']},  | Precio: {inventario['precio']},  | Cantidad: {inventario['cantidad']}  |")      

# Función para calcular estadísticas del inventario
def calcular_estadisticas():
    print("Estadísticas del Inventario:")

    if not ListaProductos:
        print("El inventario está vacío.")
        return  
    
    total_inventario = len(ListaProductos)  

    # Calcular el valor total del inventario
    valor_total = 0
    for inventario in ListaProductos:
        valor_total += inventario["precio"] * inventario["cantidad"]  

    print(f"Total de productos: {total_inventario}")
    print(f"Valor total del inventario: {valor_total}") 


# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Calcular Estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Saliendo de la app de inventario ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")




# En este proyecto se aplicaron estructuras de control,
# listas, diccionarios, validaciones y modularización
# para crear un sistema básico de inventario.
