# Dictionary to store user accounts and balances
accounts = input('Enter Your Name   \n')

# Function to display user options
def display_options():
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice

# Function to check balance
def check_balance(accounts, user):
    print("Your balance is: ", accounts[user])

# Function to withdraw
def withdraw(accounts, user, amount):
    if accounts[user] >= amount:
        accounts[user] -= amount
        print("Withdrawal successful! Your updated balance is: ", accounts[user])
    else:
        print("Insufficient funds. Your balance is: ", accounts[user])

# Function to deposit
def deposit(accounts, user, amount):
    accounts[user] += amount
    print("Deposit successful! Your updated balance is: ", accounts[user])

# Login function
def login(accounts):
    user = input("Enter your username: ")
    if user in accounts:
        print("Welcome", user)
        return user
    else:
        print("User not found. Try again.")
        return None

# Main program
user = login(accounts)
if user:
    while True:
        choice = display_options()
        if choice == 1:
            check_balance(accounts, user)
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            withdraw(accounts, user, amount)
        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))
            deposit(accounts, user, amount)
        elif choice == 4:
            print("Thank you for using our ATM. Have a great day!")
            break
        else:
            print("Invalid choice. Try again.")