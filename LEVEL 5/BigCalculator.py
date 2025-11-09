


# Lists to store numbers and operations
number_history = []
operation_history = []

# FUNCTIONS 
#We are going to define each of the functions and of course tell you what that function will return as the result
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
#In the case of division, we must warn that division between zeros is not possible.
def divide(a, b):
    if b == 0:
        return "Error: you cannot divide by zero"
    return a / b
#We created a function called show_history so we could see the entire history and print because we want to see it 
def show_history():
    print("\n--- HISTORY ---")
    for i in range(len(operation_history)): #In this case, we use `for` to display all the operations saved in the history
        print(f"{i+1}. {operation_history[i]} = {number_history[i]}")
    print("--\n")
#Now, using the `def` command, we will define the menu and use `print` to show it
def menu():
    print("ADVANCED CALCULATOR ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show history")
    print("6. Exit")

# MAIN PROGRAM 

#Next, we'll create the main loop to make the calculator work, using while for the loop, if, elif and else for the conditions, and making it clear that they are numbers with the float command
while True:
    menu()
    option = input("Choose an option (1-6): ")

    if option in ["1", "2", "3", "4"]:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if option == "1":
            result = add(a, b)
            operation = f"{a} + {b}"
        elif option == "2":
            result = subtract(a, b)
            operation = f"{a} - {b}"
        elif option == "3":
            result = multiply(a, b)
            operation = f"{a} * {b}"
        elif option == "4":
            result = divide(a, b)
            operation = f"{a} / {b}"
#here we can show the result with the command print 
        print(f"Result: {result}")
#Esta parte del programa guarda todas las operaciones que realiza el usuario. Cada operación y su resultado se almacenan en dos listas para mantener un historial

        # Save in the lists
        operation_history.append(operation)
        number_history.append(result)
#Cuando el usuario elige la opción 5, la calculadora muestra la lista de todas las operaciones y resultados. Si el usuario elige la opción 6, el programa finaliza con un mensaje de despedida
    elif option == "5":
        show_history()

    elif option == "6":
        print("Thank you for using the advanced calculator ")
        break
#Si el usuario introduce una opción no válida, el programa muestra un error y solicita que se vuelva a introducir
    else:
        print("Invalid option, please try again.")