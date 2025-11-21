
def agregar_producto(inventario, nombre, precio, cantidad):
  
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }
    inventario.append(nuevo_producto)
    print(f"--- Producto '{nombre}' agregado correctamente ---")

def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("--- El inventario está vacío ---")
    else:
        print("\n--- LISTA DE PRODUCTOS ---")
        for producto in inventario:
            calcular_total = lambda p: p["precio"] * p["cantidad"]
            total = calcular_total(producto)
            
            print(f"Nombre: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']} | Total: {total}")
        print("--------------------------")

def buscar_producto(inventario, nombre_buscado):
    for producto in inventario:
        if producto["nombre"] == nombre_buscado:
            return producto 
    else:
        return print("El producto no se encontro")
    

def actualizar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto == None:
        print("--- Error: Producto no encontrado ---")
    else:
        nuevo_precio = input("Nuevo precio (Presione Enter para no cambiar el precio): ")
        nueva_cantidad = input("Nueva cantidad (Presione Enter para no cambiar el precio: ")

        if nuevo_precio != "":
            producto["precio"] = float(nuevo_precio)
        
        if nueva_cantidad != "":
            producto["cantidad"] = int(nueva_cantidad)
            
        print("--- Producto actualizado ---")

def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print(f"--- Producto '{nombre}' eliminado ---")
    else:
        print("--- Error: Producto no encontrado ---")

def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        print("--- No hay datos para calcular estadísticas ---")
        return

    unidades_totales = 0
    valor_total = 0
    producto_mas_caro = None
    producto_mayor_stock = None
    
    
    for producto in inventario:
        unidades_totales = unidades_totales + producto["cantidad"]
        valor_total = valor_total + (producto["precio"] * producto["cantidad"])

        
        if producto_mas_caro == None or producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        if producto_mayor_stock == None or producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    print("\n--- ESTADÍSTICAS ---")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Producto con mayor stock: {producto_mayor_stock['nombre']}")