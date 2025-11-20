# Historia de Usuario
#Inventario de Productos

#funciones de gestion
import json
import csv  


#lista para almacenar los productos
ListaProductos = [] 
print("Hola, Bienvenido al Inventario de Productos")

#Guardar datos en formato JSON
def guardar_datos_json():
    with open("Inventario.json", "w") as archivo_json:
        json.dump(ListaProductos, archivo_json, indent=4)
    print("Datos guardados en Inventario.json")
#guardar datos en formato CSV        
def guardar_datos_csv():
    with open("Inventario.csv", "w", newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["Nombre", "Precio", "Cantidad"])       
        for inventario in ListaProductos:
            writer.writerow([inventario["nombre"], inventario["precio"], inventario["cantidad"]])   
    print("Datos guardados en Inventario.csv")

def guardar_datos_txt():
    with open("Inventario.txt", "w") as archivo_txt:
        for inventario in ListaProductos:
            archivo_txt.write(f"Nombre: {inventario['nombre']}, Precio: {inventario['precio']}, Cantidad: {inventario['cantidad']}\n")
    print("Datos guardados en Inventario.txt")

#leer datos desde formato JSON
def leer_datos_json():
    try:
        with open("Inventario.json", "r") as archivo_json:
            datos = json.load(archivo_json)
            ListaProductos.extend(datos)
        print("Datos cargados desde Inventario.json")
    except FileNotFoundError:
        print("No se encontró el archivo Inventario.json")
#leer datos desde formato CSV   
def leer_datos_csv():
    try:
        with open("Inventario.csv", "r") as archivo_csv:
            leer = csv.DictReader(archivo_csv)
            for row in leer:
                inventario = {
                    "nombre": row["Nombre"],
                    "precio": float(row["Precio"]),
                    "cantidad": int(row["Cantidad"])
                }
                ListaProductos.append(inventario)
        print("Datos cargados desde Inventario.csv")
    except FileNotFoundError:
        print("No se encontró el archivo Inventario.csv")
#leer datos desde formato TXT
def leer_datos_txt():
    try:
        with open("Inventario.txt", "r") as archivo_txt:
            for linea in archivo_txt:
                partes = linea.strip().split(", ")
                nombre = partes[0].split(": ")[1]
                precio = float(partes[1].split(": ")[1])
                cantidad = int(partes[2].split(": ")[1])
                inventario = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                ListaProductos.append(inventario)
        print("Datos cargados desde Inventario.txt")
    except FileNotFoundError:
        print("No se encontró el archivo Inventario.txt")
        
   

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






# En este proyecto se aplicaron estructuras de control,
# listas, diccionarios, validaciones y modularización
# para crear un sistema básico de inventario