#Agregar y eliminar frutas

frutas = ["piña","mango","fresa"] #lista de frutas inicializada con 3 elementos
while True:                      #bucle while para hacer un menú
                                #opcion va aguardar la opción de elija el usuario
    opcion = int(input(f"Qué deseas hacer con la lista de frutas: {frutas} \n1: agregar nueva fruta \n2: eliminar fruta existente \n3: salir \n"))

    # dado que son 4 opciones, hubiera hecho un switch, pero al principio lo hice sin el menu y el if, elif, else bastaba
    if opcion == 1:
        newFruta = input("Nueva fruta: ") #en newFruta se almacena la fruta que ingresa el usuario, luego con append se añade al final de la lista
        frutas.append(newFruta)
    elif opcion == 2:
        delFruta = input("Fruta a eliminar: ") #delFruta
        if delFruta in frutas: #si está la fruta en frutas, se elimina con remove
            frutas.remove(delFruta)
        else: print(f"la fruta: {delFruta} no está en {frutas}")
    elif opcion == 3: print("Fin"); break #finaliza el menu
    else: print("opción inválida") #avisa que no es una opción válida, se repite el bucle

print(frutas) #imprime la lista modificada