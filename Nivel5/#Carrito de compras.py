#Carrito de compras
carrito = []
while True:
    producto = input("Agrega un producto (o 'fin' para terminar): ")
    if producto.lower() == "fin":
        break
    carrito.append(producto)
print("Tu carrito:", carrito)