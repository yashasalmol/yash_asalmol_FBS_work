side1 = int(input("Enter a side1 : "))
side2 = int(input("Enter a side2 : "))
side3 = int(input("Enter a side3 : "))

if(side1+side2>side3 and side2+side3>side1 and side3+side1>side2):
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")