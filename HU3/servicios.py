#servicios.py
# Aquí están las funciones que manipulan la lista de productos (el inventario).

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Crea un diccionario con los datos y lo agrega a la lista.
    """
    # Creamos el diccionario
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    # Lo agregamos a la lista
    inventario.append(nuevo_producto)
    print(f"--- Producto '{nombre}' agregado correctamente ---")

def mostrar_inventario(inventario):
    """
    Recorre la lista e imprime cada producto.
    """
    if len(inventario) == 0:
        print("--- El inventario está vacío ---")
    else:
        print("\n--- LISTA DE PRODUCTOS ---")
        for producto in inventario:
            # Calculamos subtotal con una lambda simple (como pedía la tarea)
            calcular_subtotal = lambda p: p["precio"] * p["cantidad"]
            subtotal = calcular_subtotal(producto)
            
            print(f"Nombre: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']} | Subtotal: {subtotal}")
        print("--------------------------")

def buscar_producto(inventario, nombre_buscado):
    """
    Busca un producto por nombre. Retorna el diccionario si lo encuentra, o None.
    """
    for producto in inventario:
        if producto["nombre"] == nombre_buscado:
            return producto # Retornamos el producto encontrado
    return None # Si termina el ciclo y no encontró nada

def actualizar_producto(inventario, nombre):
    """
    Busca un producto y permite cambiar sus valores.
    """
    producto = buscar_producto(inventario, nombre)
    if producto == None:
        print("--- Error: Producto no encontrado ---")
    else:
        # Pedimos nuevos datos
        nuevo_precio = input("Nuevo precio (deja vacío para no cambiar): ")
        nueva_cantidad = input("Nueva cantidad (deja vacío para no cambiar): ")

        # Si el usuario escribió algo, actualizamos convertiendo a float/int
        if nuevo_precio != "":
            producto["precio"] = float(nuevo_precio)
        
        if nueva_cantidad != "":
            producto["cantidad"] = int(nueva_cantidad)
            
        print("--- Producto actualizado ---")

def eliminar_producto(inventario, nombre):
    """
    Busca un producto y lo saca de la lista.
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print(f"--- Producto '{nombre}' eliminado ---")
    else:
        print("--- Error: Producto no encontrado ---")

def calcular_estadisticas(inventario):
    """
    Calcula totales y busca el producto más caro usando variables simples.
    """
    if len(inventario) == 0:
        print("--- No hay datos para calcular estadísticas ---")
        return

    unidades_totales = 0
    valor_total = 0
    producto_mas_caro = None
    producto_mayor_stock = None
    
    # Recorremos la lista una sola vez
    for producto in inventario:
        unidades_totales = unidades_totales + producto["cantidad"]
        valor_total = valor_total + (producto["precio"] * producto["cantidad"])

        # Lógica para encontrar el más caro
        if producto_mas_caro == None or producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        # Lógica para encontrar el de mayor stock
        if producto_mayor_stock == None or producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    print("\n--- ESTADÍSTICAS ---")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Producto con mayor stock: {producto_mayor_stock['nombre']}")