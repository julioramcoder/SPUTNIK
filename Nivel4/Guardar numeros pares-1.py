# Números pares: guardar solo los pares
pares = []
for i in range(10):
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        pares.append(num)
print("Números pares:", pares)