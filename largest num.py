num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
print("The largest number is:", largest)
largest_int = int(largest)
if largest_int % 2 == 0:
    print("The largest number is even.")
else:
    print("The largest number is odd.")
