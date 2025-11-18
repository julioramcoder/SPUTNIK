#aqui inicialmente tomamos los valores iniciales para proceder con las ecuaciones 

numero1 = int(input("ingresa tu primer numero"))
numero2 = int(input("ingresa tu segundo numero"))
numero3 = int(input("ingresa tu tercer numero"))

#luego de tener los datos determinamos entre los tres numeros cual es mayor en cada operacion

mayor = max(numero1,numero2,numero3)
menor = min(numero1,numero2,numero3)

print("el numero mayor es:",mayor)
print("el numero menor es:",menor)