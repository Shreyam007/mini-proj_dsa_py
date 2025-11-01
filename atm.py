# Simple ATM Simulator in Python

balance = 10000  # starting balance
pin = "1234"

print("Welcome to Python Bank ATM!")
user_pin = input("Enter your 4-digit PIN: ")

if user_pin == pin:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Your balance is ₹{balance}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            balance += amount
            print(f"₹{amount} deposited successfully!")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= balance:
                balance -= amount
                print(f"₹{amount} withdrawn successfully!")
            else:
                print("Insufficient balance!")
        elif choice == '4':
            print("Thank you for using Python Bank ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
else:
    print("Incorrect PIN! Access denied.")
