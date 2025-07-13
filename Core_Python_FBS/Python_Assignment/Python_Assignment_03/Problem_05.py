side1 = int(input("Enter a side1 : "))
side2 = int(input("Enter a side2 : "))
side3 = int(input("Enter a side3 : "))

if(side1==side2==side3):
    print("The triangle is equilateral.")
elif(side1==side2 or side2==side3 or side3==side1):
    print("the triangle is isosceles.")
else:
    print("The triangle is scalene.")