#calculadora
numero1 = int(input("Ingresa el primer numero: "))
operador = input("Ingresa la operacion (+,-,*,/): ")
numero2 = int(input("Ingresa en el segundo numero: "))

resultado = 0

if operador == "+":
   resultado = numero1 + numero2
elif operador == "-": 
    resultado = numero1 - numero2
elif operador == "*":
  resultado =   numero1 * numero2
elif operador == "/":
   resultado = numero1 / numero2
print(f"el resultado de realizar la operacion entre {numero1} {operador} {numero2} es: {resultado}")

 