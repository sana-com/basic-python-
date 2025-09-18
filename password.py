import re
print("password must be great than 8 digit character \n"
      "must contain atleast 1 digit and 1 special character")
password=input("enter a password: ")
if len(password) <= 8:
    print(" Password must be greater than 8 characters.")

elif not re.search(r'\d', password):
    print(" Password must contain at least one digit.")

elif not re.search(r'[!@#$%]', password):
    print(" Password must contain at least one special character.")

else:
    print("Password is strong!")