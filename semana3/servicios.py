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
        with open("inventario.csv", "r") as file:
            reader = csv.DictReader(file)
            inventario = list(reader)
    except:
        inventario = []
    return inventario

def saveInventario():
    with open("inventario.csv", "w") as file:
        return
    
