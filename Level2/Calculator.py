### The user need enter the numbers ###


Number1 = float(input("Ingrese el primer número: "))
Number2 = float(input("Ingrese el segundo número: "))

### Enter the variable operation ###

operation = input("Seleccione la operación (+, -, *, /): ")

### Make operations ###

if operation == "+":
    result = Number1 + Number2
    print(f"The result of {Number1} + {Number2} is {result}")
elif operation == "-":
    result = Number1 - Number2
    print(f"The result of {Number1} - {Number2} is {result}")
elif operation == "*":
    result = Number1 * Number2
    print(f"The result of {Number1} * {Number2} is {result}")
elif operation == "/":
    if Number2 != 0:
        result = Number1 / Number2
        print(f"The result of {Number1} / {Number2} es {result}")
    else:
        print("¡Error! you cant divide by zero")
else:
    print("Operation is not valid.")