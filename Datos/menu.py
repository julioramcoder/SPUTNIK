# Menú principal

from funciones_gestion import agregar_producto, mostrar_inventario, calcular_estadisticas, guardar_datos_csv, guardar_datos_txt, leer_datos_json, leer_datos_csv, leer_datos_txt, guardar_datos_json  
def mostrar_menu():
    while True:
        print("\nMenú Principal:")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Calcular Estadísticas")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-12): ")

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
