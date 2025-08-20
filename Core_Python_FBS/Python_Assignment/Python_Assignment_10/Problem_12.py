# Write a program to create three lists of numbers, 
# their squares and cubes 

list1 = [1,2,3,4,5,6,7]
list2 = [10,20,30,40]
list3 = [90,80,70]
square = []
cube = []

list4 = list1 + list2 + list3
for i in list4:
    square.append(i**2)
    cube.append(i**3)
print("Square: ",square)
print("cube: ",cube)