#Sumatoria del 1 al n
n = int(input("Ingrese un número entero positivo: "))       
suma = 0
for i in range(1, n + 1):
    suma += i               
print("La suma del 1 al", n, "es:", suma)       