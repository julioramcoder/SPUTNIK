### First insert variable declarations starting in zero ###

suma = 0

### Second, create a loop to sum numbers until the sum is zero ###

while True:
    number = float(input("Enter a number to add to the sum (enter 0 to stop): "))

    if number == 0:
        break
    suma = suma + number

    print(f"Current sum is: {suma}")

### Finally, print the total sum ###

print(f"The total sum is: {suma}")