

frutas = ["manzana", "banana", "naranja", "pera", "uva"]

while True:
    print("\n===== MENÚ DE FRUTAS =====")
    print("1. Mostrar lista de frutas")
    print("2. Agregar una fruta")
    print("3. Eliminar una fruta")
    print("4. Buscar una fruta")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        print("\nLista de frutas:", frutas)

    elif opcion == "2":
        nueva_fruta = input("Ingresa la fruta que deseas agregar: ").strip().lower()
        if nueva_fruta in frutas:
            print(f"La fruta '{nueva_fruta}' ya está en la lista.")
        else:
            frutas.append(nueva_fruta)
            print(f"'{nueva_fruta}' fue agregada correctamente.")

    elif opcion == "3":
        fruta_eliminar = input("Ingresa la fruta que deseas eliminar: ").strip().lower()
        if fruta_eliminar in frutas:
            frutas.remove(fruta_eliminar)
            print(f"'{fruta_eliminar}' fue eliminada de la lista.")
        else:
            print(f"'{fruta_eliminar}' no se encuentra en la lista.")

    elif opcion == "4":
        fruta_buscar = input("Ingresa la fruta que deseas buscar: ").strip().lower()
        if fruta_buscar in frutas:
            print(f"'{fruta_buscar}' sí está en la lista.")
        else:
            print(f"'{fruta_buscar}' no está en la lista.")

    elif opcion == "5":
        print("Saliendo del programa... ")
        break

    else:
        print("Opción no válida. Por favor elige entre 1 y 5.")
