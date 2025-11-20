from crud import CRUD

myCrud = CRUD()
archivo = "datos.csv"

myCrud.crearArchivo(archivo)

while True:
    print("Menu")
    print("1: mostrar registro")
    print("2: agregar registro")
    print("3: modificar registro")
    print("4: eliminar registro")
    print("5: salir")

    opcion = input("elige una opción: ")

    match opcion:
        case "1":
            lista = myCrud.mostrarRegistro(archivo)
            for registro in lista:
                print(f"id: {registro[0]} nombre: {registro[1]} edad: {registro[2]}")
        case "2":
            nombre = input("oe, pone un nombre ")
            edad = int(input("edad "))
            myCrud.agregarRegistro(archivo, nombre,edad)
        case "3":
            _id = int(input("id: "))
            nombre = input("nuevo nombre: ")
            edad = int(input("nueva edad: "))
            myCrud.modificarRegistro(_id,archivo,nombre,edad)
        case "4":
            break