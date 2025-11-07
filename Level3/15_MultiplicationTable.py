### Ask the user for a number ###

number = int(input("Enter a number to see its multiplication table: "))

### Display the multiplication table from 1 to 10 ###

print(f"Multiplication table of {number}:")
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")
