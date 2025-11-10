### Initial balance for the cash machine ###

initial_balance = 1000

###list to store transaction history###

transaction_history = []

### Function to display the current balance ###

def display_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

    ### Function to deposit money ###

def deposit(balance):
    amount = float(input("Enter the amount to deposit: $"))
    if amount > 0:
        balance += amount
        transaction_history.append(f"Deposited: ${amount:.2f}")
        print(f"${amount:.2f} deposited successfully.")
    else:
        print("Deposit amount must be positive.")
    return balance

### Function to withdraw money ###

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: $"))
    if 0 < amount <= balance:
        balance -= amount
        transaction_history.append(f"Withdrew: ${amount:.2f}")
        print(f"${amount:.2f} withdrawn successfully.")
    else:
        print("Insufficient balance or invalid amount.")
    return balance

### Function to view transaction history ###

def view_transaction_history():
    if not transaction_history:
        print("No transactions yet.")
    else:
        print("Transaction History:")
        for transaction in transaction_history:
            print(f"- {transaction}")

### Main menu ###

while True:
    print("\nCash Machine Menu:")
    print("1. View Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    if choice == '1':
        display_balance(initial_balance)
    elif choice == '2':
        initial_balance = deposit(initial_balance)
    elif choice == '3':
        initial_balance = withdraw(initial_balance)
    elif choice == '4':
        view_transaction_history()
    elif choice == '5':
        print("Thank you for using the cash machine. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")