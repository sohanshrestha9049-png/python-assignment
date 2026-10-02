units = float(input("Enter electricity units consumed: "))

if units <= 20:
    bill = units * 5

elif units <= 50:
    bill = (20 * 5) + ((units - 20) * 7)

elif units <= 100:
    bill = (20 * 5) + (30 * 7) + ((units - 50) * 10)

else:
    bill = (20 * 5) + (30 * 7) + (50 * 10) + ((units - 100) * 12)

print(f"\nUnits Consumed: {units}")
print(f"Total Bill: Rs. {bill:.2f}")