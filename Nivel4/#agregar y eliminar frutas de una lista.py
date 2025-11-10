#agregar y eliminar frutas de una lista 
frutas = []
fruta = input("Agrega una fruta: ")
frutas.append(fruta)
print("Lista actual:", frutas)
eliminar = input("¿Qué fruta deseas eliminar?: ")
if eliminar in frutas:
    frutas.remove(eliminar)
print("Lista final:", frutas)
