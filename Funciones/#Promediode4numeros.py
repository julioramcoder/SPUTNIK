#Promediode4numeros
def promedio():
    suma =0
    n = int(input("Cuantos numeros quieres sumar: "))
    for i in range(n):
        suma += int(input("Ingrese numero: "))
    promedio = suma/n
    return promedio

print("El promedio es", promedio())


#Promediode4numeros
def promedio():
    suma =0
    for i in range(4):
        suma += int(input("Ingrese numero: "))
    promedio = suma/4
    return promedio

print("El promedio es", promedio())