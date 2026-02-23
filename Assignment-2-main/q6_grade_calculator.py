print("Enter marks for 5 subjects (out of 100):")

m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percent = total / 5  # percentage out of 100

# find grade based on percentage
if percent >= 90:
    grade = "A+"
elif percent >= 80:
    grade = "A"
elif percent >= 70:
    grade = "B"
elif percent >= 60:
    grade = "C"
elif percent >= 50:
    grade = "D"
else:
    grade = "F"

# fail if any subject is below 40
if m1 < 40 or m2 < 40 or m3 < 40 or m4 < 40 or m5 < 40:
    result = "FAIL"
else:
    result = "PASS"

print("\nTotal:", total, "/ 500")
print("Percentage:", round(percent, 2), "%")
print("Grade:", grade)
print("Result:", result)
