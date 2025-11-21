# app.py
import servicios
import archivos

def main():
    inventario = [] 
    archivo_nombre = "Inventario.csv"

    while True:
        cantidad = len(inventario)
        print(f"\n--- MENÚ PRINCIPAL (Tienes {cantidad} productos Guardados) ---")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Buscar Producto")
        print("4. Actualizar Producto")
        print("5. Eliminar Producto")
        print("6. Calcular Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                if precio < 0 or cantidad < 0:
                     print("Error: No se permiten números negativos")
                else:
                    servicios.agregar_producto(inventario, nombre, precio, cantidad)
            except ValueError:
                print("Error: Debes ingresar números válidos.")

        elif opcion == "2":
            servicios.mostrar_inventario(inventario)
            input("\nPresione Enter para continuar...") # Pausa para leer

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            resultado = servicios.buscar_producto(inventario, nombre)
            if resultado:
                print(f"Encontrado: {resultado}")
            else:
                print("No encontrado")
            input("\nPresione Enter para continuar...") # Pausa para leer

        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ")
            servicios.actualizar_producto(inventario, nombre)

        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ")
            servicios.eliminar_producto(inventario, nombre)

        elif opcion == "6":
            servicios.calcular_estadisticas(inventario)
            input("\nPresione Enter para continuar...") # Pausa para leer

        elif opcion == "7":
            archivos.guardar_csv(inventario, archivo_nombre)
            input("\nPresione Enter para continuar...") # Pausa para leer

        elif opcion == "8":
            datos_cargados = archivos.cargar_csv(archivo_nombre)
            if len(datos_cargados) > 0:
                respuesta = input("¿Sobrescribir inventario actual? (S/N): ")
                
                if respuesta.lower() == 's':
                    inventario = datos_cargados
                    print("--- Inventario reemplazado ---")
                else:
                
                    count_nuevos = 0
                    for nuevo in datos_cargados:
                        existente = servicios.buscar_producto(inventario, nuevo["nombre"])
                        if existente:
                            existente["cantidad"] += nuevo["cantidad"]
                            existente["precio"] = nuevo["precio"]
                        else:
                            inventario.append(nuevo)
                            count_nuevos += 1
                    print("--- Datos cargados y fusionados ---")
            input("\nPresione Enter para continuar...") # Pausa para leer

        elif opcion == "9":
            print("¡Adiós!")
            break
        
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()