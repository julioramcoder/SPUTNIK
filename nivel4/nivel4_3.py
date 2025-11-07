#Buscar un elemento en la lista.

def buscarElemento(arr,elemento):                     #como no quiero hardcodear una lista, hice una función que tiene como argumento 
                                                      # arr: arreglo, elemento: ekenebti a buscar
    if elemento in arr:
        print(f"{elemento} se encuentra en {arr}")    # si elemento está, se lo hace saber al usuario
    else: print(f"{elemento} no se encuentra en {arr}") #si no está, también le dice al usuario que no está



