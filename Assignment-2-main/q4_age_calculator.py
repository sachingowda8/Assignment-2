from datetime import date

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter birth month (1-12): "))
birth_day = int(input("Enter birth day: "))

today = date.today()
birth = date(birth_year, birth_month, birth_day)

# check if birthday already happened this year or not
age = today.year - birth_year
if (today.month, today.day) < (birth_month, birth_day):
    age = age - 1  # birthday not come yet this year

total_days = (today - birth).days

print("\nYour Age:", age, "years")
print("In months:", age * 12)
print("In days:", total_days)
print("In hours:", total_days * 24)
print("In minutes:", total_days * 24 * 60)
print("Years left to reach 100:", 100 - age)

