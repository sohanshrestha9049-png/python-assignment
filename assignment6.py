customer_name = input("Enter customer name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
membership = input("Are you a member? (yes/no): ")

subtotal = price * quantity

# Main discount
if subtotal >= 10000:
    discount_rate = 0.15
elif subtotal >= 5000:
    discount_rate = 0.10
elif subtotal >= 2000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = subtotal * discount_rate

# Additional member discount
if membership.lower() == "yes" and subtotal >= 5000:
    member_discount = subtotal * 0.05
else:
    member_discount = 0

total_discount = discount + member_discount
final_amount = subtotal - total_discount

print(f"\nCustomer Name: {customer_name}")
print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"Discount: Rs. {total_discount:.2f}")
print(f"Final Amount: Rs. {final_amount:.2f}")