### Create a empty list to store numbers ###

numbers = []

print("Enter numbers to add to the list.")
print("You can enter as many numbers as you like.(Type '0' to finish)")

### Use a loop to get numbers from the user ###

while True:
    number = float(input("Enter a number (or '0' to finish): "))
    
    if number == 0:
        break
    numbers.append(number)

### Eliminate duplicates by converting the list to a set and back to a list ###

unique_numbers = list(set(numbers))

### Finally, print the list of unique numbers ###

print(f"The list of unique numbers you entered is: {unique_numbers}")

### show the total count of unique numbers ###

removed_count = len(numbers) - len(unique_numbers)
print(f"Total duplicate numbers removed: {removed_count}")