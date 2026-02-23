num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# do all basic operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
mod = num1 % num2

# division can cause error if second number is 0
if num2 != 0:
    div = round(num1 / num2, 2)
else:
    div = "can't divide by zero"

power = num1 ** num2

print("\nResults:")
print(num1, "+", num2, "=", add)
print(num1, "-", num2, "=", sub)
print(num1, "*", num2, "=", mul)
print(num1, "/", num2, "=", div)
print(num1, "%", num2, "=", mod)
print(num1, "^", num2, "=", power)

