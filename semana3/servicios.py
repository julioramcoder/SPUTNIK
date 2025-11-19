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



import json


try:
    with open("listaInventarios.json", "r") as file:
        listInventarios = json.load(file)
except:
        listInventarios = []

def encontrarProducto(inventario: dict[str,list], nombre: str) -> dict:
    for producto in inventario["inventario"]:
        if producto["nombre"] == nombre:
            return producto
    return None

#------------------------------------Funciones para agregar producto-----------------------------------------------------------

def nuevoProducto(nombre: str, precio: float, cantidad: int) -> dict:
    return {
        "nombre" : nombre,
        "precio" : precio,
        "cantidad" : cantidad
    }

def agregarProducto(inventario: dict[str, list], nombre: str, precio: float, cantidad: int ) -> None:
    if not encontrarProducto(inventario, nombre):
        inventario["inventario"].append(nuevoProducto(nombre,precio,cantidad))
        print("producto agregado correctamente")
        return
    print(f"El producto {nombre} ya se encuentra en {inventario}"); return

def validarEntradasNuevoProducto(inventario: dict[str, list]):

    while True:
        nombre = input("Nombre del producto: ")
        if nombre.replace(" ","").isalpha():
            nombre = nombre.strip()
            break
        else: print("Ingrese un nombre válido")
    
    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio < 0: print("el precio debe ser positivo"); continue
            break
        except ValueError:
            print("Ingrese un precio válido")


    while True:
        try:
            cantidad = int(input("Cantidad de producto: "))
            if cantidad < 0: print("la cantidad debe ser positiva"); continue
            break
        except ValueError:
            print("Ingrese una cantidad válida")
    
    print(f"{nombre}, precio: {precio}, cantidad: {cantidad}")
    agregarProducto(inventario,nombre,precio,cantidad)
    

#----------------------------------Funciones para crear nuevo inventario---------------------------------------------

def crearNuevoInventario(nombre: str) -> dict:
    return {
        "nombre" : nombre,
        "inventario" : []
    }

def agregarNuevoInventario(nombre):
    for inventario in listInventarios:
        if inventario["nombre"] == nombre:
            print(f"Ya existe un inventario con el nombre_ {nombre}")
            return
        listInventarios.append()
        



