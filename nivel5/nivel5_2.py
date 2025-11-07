#Carrito de compras.

class item:
    def __init__(self,itemName,itemPrice,itemCount):   #Es exacatanebte igual a la estructura que tengo enel problema de sistema de notas
        self.itemName = itemName                       #incluso las variables las nombre igual porque reutilicé el código anterior
        self.itemPrice = itemPrice                     #solo cambié la salida y las propiedades de la clase
        self.itemCount = itemCount
        self.total = itemCount*itemPrice

lista = []                                           #en esta lista voy a guardar las instancias/objetos de la clase nota
while True:                                          #bucle while para hacer el menu
    option = int(input("1: Para agregar un nuevo item \n2: para salir\n"))

    if option == 1:                                          #toma los datos
        newEstudiante = input("Nombre del producto: ")
        newNota1 = float(input("precio: "))
        newNota2 = float(input("cantidad: "))
        nuevoNota = item(newEstudiante,newNota1,newNota2)   #con los datos construye un objeto de tipo nota
        lista.append(nuevoNota)                             #una vez construido, lo agrega a lista
    elif option == 2:                                       #esta opción sale del bucle
        break
    else:print("opcion incorrecta")

for el in lista: #al finalizar, se muestra la info del estudiante
    print(f"Producto {el.itemName} | precio: {el.itemPrice} | cantidad {el.itemCount}| total: {el.total}")
        