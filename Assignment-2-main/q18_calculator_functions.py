def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: division by zero"
    return a % b

def power(a, b):
    return a ** b

def calculator():
    while True:
        print("\n--- Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        ch = input("Choose: ")

        if ch == "7":
            print("Goodbye!")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if ch == "1":
            print("Result:", add(a, b))
        elif ch == "2":
            print("Result:", subtract(a, b))
        elif ch == "3":
            print("Result:", multiply(a, b))
        elif ch == "4":
            print("Result:", divide(a, b))
        elif ch == "5":
            print("Result:", modulus(a, b))
        elif ch == "6":
            print("Result:", power(a, b))
        else:
            print("Invalid choice")

calculator()

