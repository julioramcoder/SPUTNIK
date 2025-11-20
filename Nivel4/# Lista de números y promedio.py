# Lista de números y promedio
numeros = []
for i in range(5):
    n = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(n)
promedio = sum(numeros) / len(numeros)
print("El promedio es:", promedio)