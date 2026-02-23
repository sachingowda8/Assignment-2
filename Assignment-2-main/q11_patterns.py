print("Choose a pattern:")
print("1. 1 / 1 2 / 1 2 3 ...")
print("2. 1 / 2 2 / 3 3 3 ...")
print("3. Inverted countdown")
print("4. Palindrome triangle")

choice = input("Your choice: ")
n = int(input("Height: "))

if choice == "1":
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

elif choice == "2":
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()

elif choice == "3":
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

elif choice == "4":
    for i in range(1, n+1):
        row = ""
        for j in range(1, i+1):
            row += str(j)
        for j in range(i-1, 0, -1):
            row += str(j)
        print(row)

else:
    print("Invalid choice")

