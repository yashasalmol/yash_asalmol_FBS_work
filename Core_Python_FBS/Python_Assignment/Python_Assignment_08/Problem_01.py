def AreaRect(length,width):
    area = length * width
    return area
length = int(input("Enter a length : "))
width = int(input("Enter a breadth : "))
result = AreaRect(length,width)
print(result)