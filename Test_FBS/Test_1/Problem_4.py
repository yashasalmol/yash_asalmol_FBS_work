Length = int(input("Enter Length of Wall: "))
Breadth = int(input("Enter Breadth of Wall: "))
Cost = int(input("Enter Cost Of Colour per Unit: "))

Area = Length * Breadth
Allwalls = Area * 4
CostOfPaint = Allwalls * Cost

print("Total Cost of Painting 4 Walls is: ₹", CostOfPaint)