from permanenciaDatos import *
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

def ingresarDatosProducto():
    nombre = validarNombre()
    precio = validarPrecio()
    cantidad = validarCantidad()
    agregarProducto(nombre,precio,cantidad)

#--------------------------------------------------------------------------------------------------------------

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
def mostrarInventario() -> None:
    print(f"{'nombre' :<15} {'precio':<15} {'cantidad' :<15}")
    for producto in inventario:
        print(f"{producto['nombre']:<15} {producto['precio']:<15} {producto['cantidad']:<15}")

def mostrarProducto(nombre: str) -> None:
    producto = buscarProducto(nombre)
    if producto:
        print(f"{'nombre':<15} {'precio':<15} {'cantidad':<15}")
        print(f"{producto['nombre']:<15} {producto['precio']:<15} {producto['cantidad']:<15}")

#------------------------------------------------------------------------------------------

def actualizarProducto(nombre :str, nuevoPrecio :float = None, nuevaCantidad : int = None) -> dict:
    producto = buscarProducto(nombre)
    if producto:
        if nuevoPrecio:
            producto["precio"] = nuevoPrecio
        if nuevaCantidad:
            producto["cantidad"] = nuevaCantidad
    return producto

def actualizarProductoMenu():
    nombre = validarNombre()
    if not buscarProducto(nombre):
        print(f"No se puede actualizar el producto {nombre} ya que no está en el inventario")
        return
    opcion = input(f"Actualizar precio de {nombre} (s/n): ")
    if opcion == "s":
        precio = validarPrecio()
    else: precio = None
    opcion = input(f"Actualizar cantidad de {nombre} (s/n): ")
    if opcion == "s":
        cantidad = validarCantidad()
    else: cantidad = None
    actualizarProducto(nombre,precio,cantidad)
    saveInventario(inventario)
    
#------------------------------------------------------------------------------------------
def eliminarProducto(nombre : str):
    producto = buscarProducto(nombre)
    if producto:
        inventario.remove(producto)
        saveInventario(inventario)
    

#-----------------------------------------------------------------------------------------


def unidadesTotales() -> int:
    totalUnidades = 0
    if inventario:
        for producto in inventario:
            totalUnidades += producto["cantidad"]
        return totalUnidades
    return None

def valorTotal() -> float:
    totalValor = 0
    if inventario:
        for producto in inventario:
            precioTotalProducto = producto["cantidad"] * producto["precio"] 
            totalValor += precioTotalProducto
        return totalValor
    return None

def productoMasCaro() -> dict:
    masCaro = 0
    productoReturn : dict = None
    if inventario:
        for producto in inventario:
            if masCaro < producto["precio"]:
                masCaro = producto["precio"]
                productoReturn = producto
    return productoReturn
    
def mayorStock():
    masStack = 0
    productoReturn : dict = None
    if inventario:
        for producto in inventario:
            if masStack < producto["cantidad"]:
                masStack = producto["cantidad"]
                productoReturn = producto
    return productoReturn
    


def estadisticas():
    return


