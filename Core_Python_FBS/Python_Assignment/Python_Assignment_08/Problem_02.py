# Write a program to calculate area of circle 

def CalCircle(r):
    area = 3.14 * r * r
    return area

radius = int(input("Enter a radius : "))
x=CalCircle(radius)
print(x)