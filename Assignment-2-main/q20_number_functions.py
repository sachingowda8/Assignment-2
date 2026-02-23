def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b

def sum_of_digits(n):
    total = 0
    for d in str(abs(n)):
        total += int(d)
    return total

def reverse_number(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == n

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_perfect_number(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

def math_menu():
    while True:
        print("\n--- Number Functions Menu ---")
        print("1. Factorial")
        print("2. Is Prime")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Is Armstrong")
        print("7. GCD")
        print("8. LCM")
        print("9. Is Perfect Number")
        print("10. Exit")

        ch = input("Choose: ")

        if ch == "10":
            print("Bye!")
            break
        elif ch == "1":
            n = int(input("Enter n: "))
            print("Factorial:", factorial(n))
        elif ch == "2":
            n = int(input("Enter number: "))
            print("Prime:", is_prime(n))
        elif ch == "3":
            n = int(input("Enter position: "))
            print("Fibonacci:", fibonacci(n))
        elif ch == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))
        elif ch == "5":
            n = int(input("Enter number: "))
            print("Reversed:", reverse_number(n))
        elif ch == "6":
            n = int(input("Enter number: "))
            print("Armstrong:", is_armstrong(n))
        elif ch == "7":
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print("GCD:", gcd(a, b))
        elif ch == "8":
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print("LCM:", lcm(a, b))
        elif ch == "9":
            n = int(input("Enter number: "))
            print("Perfect Number:", is_perfect_number(n))
        else:
            print("Invalid choice")

math_menu()

