import sys
sys.stdout.reconfigure(encoding='utf-8')

year = int(input("Enter a year: "))

# leap year rules: divisible by 4, but not 100, unless also 400
if year % 400 == 0:
    print(year, "is a Leap Year (divisible by 400)")
elif year % 100 == 0:
    print(year, "is NOT a Leap Year (divisible by 100 but not 400)")
elif year % 4 == 0:
    print(year, "is a Leap Year (divisible by 4)")
else:
    print(year, "is NOT a Leap Year")
