import sys
sys.stdout.reconfigure(encoding='utf-8')

balance = 10000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        print("Your balance is:", balance)
    elif ch == "2":
        amt = float(input("Enter deposit amount: "))
        if amt <= 0:
            print("Amount must be positive")
        else:
            balance = balance + amt
            print("Deposited! New balance:", balance)
    elif ch == "3":
        amt = float(input("Enter withdraw amount: "))
        # minimum 500 should stay in account
        if amt <= 0:
            print("Amount must be positive")
        elif balance - amt < 500:
            print("Cannot withdraw. Minimum balance of 500 must remain.")
            print("You can withdraw max:", balance - 500)
        else:
            balance = balance - amt
            print("Withdrawn! New balance:", balance)
    elif ch == "4":
        print("Thank you! Goodbye.")
        break
    else:
        print("Invalid choice")

