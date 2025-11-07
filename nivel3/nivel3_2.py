#Sumatoria del 1 al n.

numero = int(input("¿hasta qué número quieres sumar? ")) # se pide al usuario el "n"
suma = 0                                                 # la variabe suma se va actualizando en cada ciclo
for i in range(numero + 1):                              # el bucle va hasta "numero + 1" para que también se incluya "numero"
    suma += i                                            # en cada ciclo suma se agrega a sí mismo el valor que tenga i en ese ciclo
print(f"La suma de los primeros {numero} números naturales es: {suma}") # se muestra al usuario el resultado 
                                                         # Nota: este algorimo da la respuesta en O(n), se puede hacer en 0(1)
                                                         # usando la fórmula de Gauss, pero no la uso porque estamos practicando bucles
