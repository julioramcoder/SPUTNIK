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
print(menu)

#--------------------------Task 2-----------------------------------
"""
2. Implementar un bucle para múltiples registros:
Envuelve el menú en un bucle while que continúe ejecutándose hasta que el usuario elija salir.
Permite agregar varios productos seguidos (nombre, precio y cantidad).
Cada producto debe almacenarse como un diccionario dentro de una lista llamada inventario.
producto = {"nombre": "Lápiz", "precio": 500, "cantidad": 3}
inventario.append(producto)"""