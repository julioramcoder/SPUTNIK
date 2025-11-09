### Add a fruits to the list ###

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("Original list of fruits:", fruits)

### Ask the user to add a fruit ###

new_fruit = input("Enter a fruit to add to the list: ").lower()
fruits.append(new_fruit)
print("Updated list of fruits after addition:", fruits)

### Loop display fruits with their indices ###

print("\ncurrent fruits in the list:")
for fruit in fruits:
    print(f"- {fruit}")

### Ask the user to delete a fruit by its name ###

remove_fruit = input("\nEnter the name of the fruit to remove from the list: ").lower()

### Check if the fruit is in the list and remove it ###

if remove_fruit in fruits:
    fruits.remove(remove_fruit)
    print(f"{remove_fruit} has been removed from the list.")
else:
    print(f"{remove_fruit} is not in the list.")

    ### Final list of fruits showing ###

print("Final list of fruits:", fruits)