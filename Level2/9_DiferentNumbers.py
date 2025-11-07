# Request three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare to find the largest and smallest
largest = num1
smallest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3

# Display the results
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
