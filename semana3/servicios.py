"""2. Estructura de datos y modularización:
Mantén un inventario en memoria como lista de diccionarios, donde cada producto tenga:
{"nombre": str, "precio": float, "cantidad": int}
Crea un archivo principal app.py y un módulo servicios.py (o nombres equivalentes) con funciones:
agregar_producto(inventario, nombre, precio, cantidad)
mostrar_inventario(inventario)
buscar_producto(inventario, nombre) → retorna el dict o None
actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
eliminar_producto(inventario, nombre)
calcular_estadisticas(inventario) → retorna tupla/dict con métricas
Documenta cada función con docstring (qué hace, parámetros, retorno) y agrega comentarios breves."""





import csv
def loadInventario() -> list[dict]:
    try:
        with open("inventario.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            inventario = list(reader)         
    except:
        inventario = []
    return inventario

inventario = loadInventario()


def saveInventario(inventario : list[dict]):
    try:
        with open("inventario.csv", "w", newline="", encoding="utf-8") as file:
            if inventario:
                fields = inventario[0].keys()
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(inventario)
    except: print("error al guardar inventario")

#------------------------------------------------------------------------------------------------------------------
def crearProducto(nombre:str, precio: float, cantidad: int) -> dict:
    producto = {
        "nombre" : nombre,
        "precio" : precio,
        "cantidad" : cantidad
    }    

    return producto

def buscarProducto(nombre: str) -> dict:
    for producto in inventario:
        if producto["nombre"] == nombre:
            print(f"producto {nombre} ya se encuentra en el inventario")
            return producto
            
    return None

def agregarProducto(nombre: str, precio: float, cantidad: int) -> None:
    if not buscarProducto(nombre):
        producto = crearProducto(nombre, precio, cantidad)
        inventario.append(producto)
        saveInventario(inventario)
        return
    
    return


def validarNombre() -> str:
    name : str
    while True:
        name = input("Nombre del producto: ")
        if name.replace(" ", "").isalpha():
            return name
        else: print("nombre inválido")
        
def validarPrecio() -> float:
    while True:
        try:
            precio = float(input("precio del producto: "))
            return precio
        except ValueError:
            print("ingrese un precio válido ")

def validarCantidad() -> int:
    while True:
        try:
            cantidad = int(input("cantidad del producto: "))
            return cantidad
        except ValueError:
            print("ingrese una cantidad válida ")

#-----------------------------------------------------------------------------------------
def mostrarInventario():
    print(f"{'nombre' :<15} {'precio':<15} {'cantidad' :<15}")
    for producto in inventario:
        print(f"{producto['nombre']:<15} {producto['precio']:<15} {producto['cantidad']:<15}")
#------------------------------------------------------------------------------------------

def ingresarDatosProducto():
    nombre = validarNombre()
    precio = validarPrecio()
    cantidad = validarCantidad()
    agregarProducto(nombre,precio,cantidad)

while True:
    print("1: agregar nuevo producto")
    print("2: monstrar inventario")
    print(": salir")

    opcion = input(": ")
    if opcion == "1":
        ingresarDatosProducto()
    elif opcion == "2":
        mostrarInventario()
    elif opcion == "3":
        break
    else: print("opción inválida")
    




