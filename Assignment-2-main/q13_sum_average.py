n = int(input("How many numbers? "))

nums = []
for i in range(1, n+1):
    x = float(input("Enter number " + str(i) + ": "))
    nums.append(x)

total = 0
for x in nums:
    total = total + x

avg = total / n
big = nums[0]
small = nums[0]

for x in nums:
    if x > big:
        big = x
    if x < small:
        small = x

print("\nSum:", total)
print("Average:", avg)
print("Maximum:", big)
print("Minimum:", small)
