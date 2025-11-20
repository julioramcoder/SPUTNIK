from crud import CRUD


crud = CRUD()
archivo = "datos.csv"

crud.crear_archivo(archivo)

while True:
    print("\n--- MENU ---")
    print("1. Crear persona")
    print("2. Listar personas")
    print ("3. Editar persona")
    print("4. Eliminar persona")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = input("Edad: ")

        id_creado = crud.crear(archivo, nombre, edad)
        print(f"Persona creada con ID: {id_creado}")

    elif opcion == "2":
        datos = crud.listar(archivo)
        print("\n--- LISTADO ---")
        for fila in datos:
            print(f"ID: {fila[0]} | Nombre: {fila[1]} | Edad: {fila[2]}")
    elif opcion == "3":
        id_persona = input("ID de la persona a editar: ")
        nuevo_nombre = input("Nuevo nombre: ")
        nueva_edad = input("Nueva edad: ")
        if crud.editar(archivo, id_persona, nuevo_nombre, nueva_edad):
            print("Persona editada exitosamente.")
        else: 
            print("No se encontró la persona con ese ID.")
                

    elif opcion == "4": 
       id_eliminar = input("ID de la persona a eliminar: ")

       if crud.eliminar(archivo, id_eliminar):
           print("Persona eliminada exitosamente.") 
        
       else:
            print("No se encontró la persona con ese ID.")

    elif opcion == "5":
        print("Saliendo del programa.") 
    else:
        print("Opción no válida. Intenta de nuevo.")
        break
        
   




