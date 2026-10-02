balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))
pin = input("Enter PIN: ")

correct_pin = "1234"

if pin != correct_pin:
    print("Invalid PIN")

elif withdrawal <= 0:
    print("Invalid withdrawal amount")

elif withdrawal > balance:
    print("Insufficient balance")

else:
    remaining_balance = balance - withdrawal

    print("\nWithdrawal successful!")
    print(f"Withdrawal Amount: Rs. {withdrawal:.2f}")
    print(f"Remaining Balance: Rs. {remaining_balance:.2f}")
    