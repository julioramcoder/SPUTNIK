#solicitamos un valor inicial para proceder con la multiplicacion
numero = int(input("ingresa un numero"))
#luego de esto tomamos elvalor ingresado y lo multiplicamos por el valor siguente
print(f"/ntabla de multiplicar del {numero} :")
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")