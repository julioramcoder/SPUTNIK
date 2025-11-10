###List to store items in the shopping cart###

cart = []

### function to display the shopping cart items ###

def add_item():
    name = input("Enter the name of the item to add: ")
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity of the item: "))

    ###each item is represented as a dictionary ###

    cart.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })
    print(f"{quantity} of {name} added to the cart.")

### function to display the shopping cart items ###
def view_cart():
    if not cart:
        print("Your shopping cart is empty.")
        return

    print("\nItems in your shopping cart:")
    for index, item in enumerate(cart, start=1):
        print(f"{index}. {item['name']} - ${item['price']} x {item['quantity']}")

    total = sum(item['price'] * item['quantity'] for item in cart)
    print(f"\nTotal amount: ${total:.2f}")

### function to remove an item from the cart ###
def remove_item():
    view_cart()
    if not cart:
        return

    item_index = int(input("Enter the item number to remove from the cart: ")) - 1

    if 0 <= item_index < len(cart):
        removed_item = cart.pop(item_index)
        print(f"Removed {removed_item['name']} from the cart.")
    else:
        print("Invalid item number.")

### function to clear the cart ###
def clear_cart():
    cart.clear()
    print("Shopping cart has been cleared.")

### Main loop to interact with the shopping cart ###

while True:
    print("\nShopping Cart Menu:")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Clear Cart")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        view_cart()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        clear_cart()
    elif choice == '5':
        print("Exiting the shopping cart. Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please try again.")

        ### End of Shopping Cart Program ###