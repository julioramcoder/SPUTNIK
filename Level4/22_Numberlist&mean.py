### Create a empty list to store numbers ###

number_list = []

print("Enter numbers to add to the list.")
print("You can enter as many numbers as you like.(Type '0' to finish)")

### Use a loop to get numbers from the user ###

while True:
    number = float(input("Enter a number (or '0' to finish): "))
    
    if number == 0:
        break
    number_list.append(number)

### Calculate the mean of the numbers in the list ###

if len(number_list) == 0:
    print("No numbers were entered.")

else:

    ### If there are numbers, calculate and print the mean ###

    mean = sum(number_list) / len(number_list)

    ### Finally, print the list and the mean ###

    print(f"The mean of the entered numbers {number_list} is: {mean}")
