#buscar elemento en una lista   
frutas = ["manzana", "pera", "banana", "uva"]
buscar = input("¿Qué fruta quieres buscar?: ")
if buscar in frutas:
    print("Sí, está en la lista.")
else:
    print("No está en la lista.")