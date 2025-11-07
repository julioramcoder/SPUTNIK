#Números pares: guardar solo los pares

pares = []                     #lista donde se van a almacenar los numeros pares

def addPar(numero):            #función addPar, recibe como argumento "numero" 
    if numero % 2 == 0:        #si "numero" es par, entonces se agrega a la lista
        pares.append(numero)

for i in range(21):            #for para probar 20 veces la función addpar, con los números del 1 al 20
    addPar(i)

print(pares)                   #se muestra al usuario


