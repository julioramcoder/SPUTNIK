# Lista original de números (puedes modificarla o hacer que el usuario la ingrese)
numeros = [1, 2, 3, 4, 5, 6, 2, 4, 8, 10, 10, 3, 12]

print("Lista original:", numeros)

# 1. Filtrar solo los números pares
pares = [n for n in numeros if n % 2 == 0]
print("Números pares:", pares)

# 2. Eliminar duplicados usando 'set'
pares_sin_duplicados = list(set(pares))
print("Números pares sin duplicados:", pares_sin_duplicados)

# 3. (Opcional) Ordenar la lista final
pares_sin_duplicados.sort()
print("Lista final ordenada:", pares_sin_duplicados)
