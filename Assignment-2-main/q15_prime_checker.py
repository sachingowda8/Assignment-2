n = int(input("Enter a number: "))

# handle edge cases first
if n < 2:
    print(n, "is NOT prime")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is PRIME")
    else:
        print(n, "is NOT prime")

# part 2 - find all primes in a range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

primes = []
for num in range(start, end+1):
    if num < 2:
        continue
    ok = True
    for i in range(2, num):
        if num % i == 0:
            ok = False
            break
    if ok:
        primes.append(num)

print("Primes between", start, "and", end, ":", primes)

