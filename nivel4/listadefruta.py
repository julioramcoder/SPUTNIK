# Lista de frutas
frutas = ["manzana", "banana", "naranja", "pera", "uva", "kiwi"]

# Imprimir la lista completa
print("Lista de frutas:", frutas)

# Acceder a un elemento específico
print("Primera fruta:", frutas[0])

# Agregar una fruta
frutas.append("mango")
print("Después de agregar mango:", frutas)

# Eliminar una fruta
frutas.remove("pera")
print("Después de eliminar pera:", frutas)

# Ordenar la lista alfabéticamente
frutas.sort()
print("Lista ordenada:", frutas)

# Recorrer la lista
print("Frutas una por una:")
for fruta in frutas:
    print("-", fruta)
