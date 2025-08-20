x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x == 0 and y == 0:
    print("The point lies at the Origin.")
elif x == 0:
    print("The point lies on the Y-axis.")
elif y == 0:
    print("The point lies on the X-axis.")
elif x > 0 and y > 0:
    print("The point lies in the 1st Quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the 2nd Quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the 3rd Quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the 4th Quadrant.")

