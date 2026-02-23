bill = float(input("Enter total bill: "))
people = int(input("Number of people: "))
tax = float(input("Tax percentage: "))
tip = float(input("Tip percentage: "))

# calculate step by step
tax_amount = bill * tax / 100
after_tax = bill + tax_amount
tip_amount = after_tax * tip / 100
total = after_tax + tip_amount
per_person = total / people

print("\n=== BILL BREAKDOWN ===")
print("Subtotal:   ", round(bill, 2))
print("Tax (" + str(tax) + "%):  ", round(tax_amount, 2))
print("After tax:  ", round(after_tax, 2))
print("Tip (" + str(tip) + "%):  ", round(tip_amount, 2))
print("Total:      ", round(total, 2))
print("Per person: ", round(per_person, 2))
