#Eliminar duplicados

def eliminarDuplicados(lista):        #defino la funcion eliminarDuplicados, donde el argumento lista es una lista de elementos
    unicos  = []                      #unicos es una lista en donde se va a guardar los elementos unicos
    repetidos = []                    #repetidos es una lista en donde se van a guardar los elementos repetidos
    for el in lista:                  #por cada elemento "el" de la lista
        if el not in unicos:          # si el elemento no esta actualmente en la lista de unicos, se agrega
            unicos.append(el)
        else: repetidos.append(el)    #si el elemmento ya está en unicos, se agrega a la lista de repetidos
    
    for el in repetidos:              #aquí quería usar el método remove, para eliminar los repoetidos, pero realmente
        lista.remove(el)              #en la lista de unicos ya no hay repetidos y basta con retornar/imprimir unicos
    print(lista)

eliminarDuplicados([1,2,3,4,5,6,2,3]) #ejemplo de uso



