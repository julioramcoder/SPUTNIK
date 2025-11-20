from servicios import ingresarDatosProducto, mostrarInventario, actualizarProductoMenu,eliminarProducto,validarNombre, mostrarProducto


def saltoDeLinea():
    print("---------------------------------------------\n")
while True:
    saltoDeLinea()
    print("1: agregar nuevo producto")
    print("2: monstrar inventario")
    print("3: monstrar producto")
    print("4: actualizar producto")
    print("5: eliminar producto")
    print("6: estadisticas")
    print("7: generar informe")
    print("6: salir")

    opcion = input()
   
    match opcion:
        case "1":
            saltoDeLinea()
            print("agregar nuevo producto\n")
            ingresarDatosProducto()
            saltoDeLinea()
        case "2":
            saltoDeLinea()
            print("mostrar inventario")
            mostrarInventario()
            saltoDeLinea()
        case "3":
            saltoDeLinea()
            print("mostrar producto")
            nombre = validarNombre()
            mostrarProducto(nombre)
            saltoDeLinea()
        case "4":
            saltoDeLinea()
            print("acutalizar producto")
            actualizarProductoMenu()
            saltoDeLinea()
        case "5":
            saltoDeLinea()
            print("eliminar producto")
            nombre = validarNombre()
            eliminarProducto(nombre)
            saltoDeLinea()
        case "6":
            break
        case  _case:
            print("opción inválida")
            saltoDeLinea()
            
    
