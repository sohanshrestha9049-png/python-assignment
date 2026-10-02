num = int(input("Enter an integer: "))

# Positive, negative or zero
if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"

# Even or odd
if num % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"

# Divisible by 3
if num % 3 == 0:
    divisible_3 = "Yes"
else:
    divisible_3 = "No"

# Divisible by 5
if num % 5 == 0:
    divisible_5 = "Yes"
else:
    divisible_5 = "No"

# Divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    both = "Yes"
else:
    both = "No"

print(f"\nNumber: {num}")
print(f"Type: {sign}")
print(f"Even or Odd: {even_odd}")
print(f"Divisible by 3: {divisible_3}")
print(f"Divisible by 5: {divisible_5}")
print(f"Divisible by both 3 and 5: {both}")
