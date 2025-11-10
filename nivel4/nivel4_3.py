#Buscar un elemento en la lista.

def buscarElemento(arr,elemento):                     #como no quiero hardcodear una lista, hice una función que tiene como argumento 
                                                      # arr: arreglo, elemento: ekenebti a buscar
    if elemento in arr:
        print(f"{elemento} se encuentra en {arr}")    # si elemento está, se lo hace saber al usuario
    else: print(f"{elemento} no se encuentra en {arr}") #si no está, también le dice al usuario que no está


    #-----------version sin "trampa"------------------------

    def BuscarElementoBien(arr,elemento):   #nueva función
        encontrado = False                  #inicialmente, se define "encontrado" como falso
        for i in range(len(arr) - 1):       #bucle for, desde 0 hasta n - 1       
            if arr[i] == elemento:          #si solo un elemento de "arr" es igual a "elemento", se encontró, no hace falta seguir buscando
                encontrado = True; break
        return encontrado                   #se retorna el booleano encontrado (false si no se encuentra, true si sí)
    #modifiqué la función porque no quería usar la linea: "if elemento in arr" porque es como hacer trampa, usar una función para hacer la misma función que me piden hacer


