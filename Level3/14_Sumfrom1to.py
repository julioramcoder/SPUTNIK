### Ask the user for a positive integer n ###

n = int(input("Enter a positive integer n: "))

### Initialize the sum ###

total = 0

### Calculate the sum from 1 to n ###

for number in range(1, n + 1):
    total += number

### Display the result ###

print(f"The sum of numbers from 1 to {n} is {total}.")
