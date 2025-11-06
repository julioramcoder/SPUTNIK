#Comparador de tres números: mayor y menor.
numeros = [] #inicio un arreglo en el que voy a almacenar los 3 números

for i in range(3): #inicio bucle for, i tendrá los valors 0,1 y 2
    newNum = int(input(f"ingresa el número {i + 1}: ")) #en cada loop se pide un número
    numeros.append(newNum)                              #el nuevo número es agregado al arrelo numeros

max = numeros[0]   #la variable max es el primer elemento del arreglo

for numero in numeros: #en este bucle itero por los elementos, no los índices
    if max < numero: max = numero #si max es menos que uno de los elementos, entonces no es el max, por lo tanto lo actualizo



min = numeros[0] #misma lógica que con máx, salvo la condicón en lugar de preguntar si es menor, pregunto si es mayor

for numero in numeros:
    if min > numero: min = numero

print(f"de los números {numeros} el menor es: {min} y el mayor es {max}") #se muestran los resultados al usuario
