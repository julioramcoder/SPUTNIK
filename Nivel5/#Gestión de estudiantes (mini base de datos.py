#Gestión de estudiantes (mini base de datos)
estudiantes = []
while True:
    print("\n1. Agregar estudiante\n2. Ver lista\n3. Buscar estudiante\n4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        edad = int(input("Edad: "))
        estudiantes.append({"nombre": nombre, "edad": edad})
    elif opcion == "2":
        print("Lista de estudiantes:")
        for e in estudiantes:
            print(e)
    elif opcion == "3":
        buscar = input("Nombre a buscar: ")
        encontrado = False
        for e in estudiantes:
            if e["nombre"].lower() == buscar.lower():
                print(e)
                encontrado = True
        if not encontrado:
            print("No encontrado.")
    elif opcion == "4":
        break