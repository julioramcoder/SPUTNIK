#Lista de números y promedio.

def prom(lista):                        #función prom recibe como argumento una lista
    suma = 0                            #suma va a guardar la suma de todos los elementos de la lista
    for el in lista:                    #for iterando por los elementos de la lista
        suma += el                      #se va incrementando suma según el valor actal de "el"
    return suma/len(lista)              #retorno el promedio, divido la suma entre la cantidad de elementos de la lista

promedio = prom([1,2,4,2,6,7])         #ejemplo de uso
print(promedio)