age = int(input("Enter age: "))
day = input("Enter day (e.g. Monday): ").strip().lower()
tickets = int(input("Number of tickets: "))

# set price based on age group
if age < 3:
    price = 0
    category = "Free"
elif age <= 12:
    price = 150
    category = "Child"
elif age <= 59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"

# weekend gets 20% off
weekend = ["friday", "saturday", "sunday"]
if day in weekend:
    discount = price * 20 / 100
else:
    discount = 0

final_price = price - discount
total = final_price * tickets

print("\nCategory:", category)
print("Base Price:", price)
print("Discount:", discount)
print("Price after discount:", final_price)
print("Total for", tickets, "ticket(s):", total)
