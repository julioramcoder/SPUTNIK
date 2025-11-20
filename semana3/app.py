from servicios import ingresarDatosProducto, mostrarInventario, actualizarProductoMenu,eliminarProducto,validarNombre, mostrarProducto



while True:
    print("1: agregar nuevo producto")
    print("2: monstrar inventario")
    print("3: monstrar producto")
    print("4: actualizar producto")
    print("5: eliminar producto")
    print("6: salir")

    opcion = input(" ")
    if opcion == "1":
        ingresarDatosProducto()
    elif opcion == "2":
        mostrarInventario()
    elif opcion == "3":
        nombre = validarNombre()
        mostrarProducto(nombre)
    elif opcion == "4":
        actualizarProductoMenu()
    elif opcion == "5":
        nombre = validarNombre()
        eliminarProducto(nombre)
    elif opcion == "6":
        break
    else: print("opción inválida")
    
