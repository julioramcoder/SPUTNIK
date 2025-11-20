#Agenda de contactos
agenda = []
while True:
    print("\n1. Agregar contacto\n2. Ver contactos\n3. Buscar\n4. Eliminar\n5. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda.append({"nombre": nombre, "teléfono": telefono})
    elif opcion == "2":
        for c in agenda:
            print(c)
    elif opcion == "3":
        buscar = input("Nombre a buscar: ")
        for c in agenda:
            if c["nombre"].lower() == buscar.lower():
                print(c)
    elif opcion == "4":
        eliminar = input("Nombre a eliminar: ")
        agenda = [c for c in agenda if c["nombre"].lower() != eliminar.lower()]
        print("Contacto eliminado.")
    elif opcion == "5":
        break