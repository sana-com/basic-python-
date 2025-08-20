side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))
if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print("It is a valid triangle.")
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The given sides do not form a valid triangle.")

