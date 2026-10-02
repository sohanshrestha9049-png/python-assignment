username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "admin123":
        role = "Administrator"
        print(f"Role: {role}")
        print("Full system access")
    else:
        print("Invalid username or password")

elif username == "student12":
    if password == "study123":
        role = "Student"
        print(f"Role: {role}")
    else:
        print("Invalid username or password")

else:
    print("Invalid username or password")
    