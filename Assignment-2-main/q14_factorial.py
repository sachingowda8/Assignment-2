n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
elif n == 0:
    print("0! = 1")
else:
    result = 1
    steps = str(n)
    for i in range(n-1, 0, -1):
        result = result * i
        steps = steps + " x " + str(i)
    print(str(n) + "! =", steps, "=", result)

