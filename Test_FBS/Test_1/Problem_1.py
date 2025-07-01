length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))
radius = float(input("Enter the radius of semicircle: "))
#calculate area
rectangle_area = length * breadth
semicircle_area = (3.14 * radius**2)/2
total_area = rectangle_area + semicircle_area
#Calculate perimeter
rectangle_perimeter = 2 * length* breadth
semicircule_perimeter = (3.14 * radius * radius) / 2
total_perimeter = rectangle_area + semicircle_area

print("total Area :",total_area)
print("Total Perimeter :",total_perimeter)