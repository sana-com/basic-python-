def greater_num (a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a = int(input("enter the 1st number: "))
b = int(input("enter the 2nd number: "))
c = int(input("enter the 3rd number: "))

print("greatest number is:", greater_num(a, b, c))

