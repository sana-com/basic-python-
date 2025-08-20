stored_username = "student"
stored_password = "stu23@nshm"
input_username = input("Enter username: ")
input_password = input("Enter password: ")
if input_username == stored_username and input_password == stored_password:
    print("Valid username and password.")
else:
    print("Invalid username or password.")

