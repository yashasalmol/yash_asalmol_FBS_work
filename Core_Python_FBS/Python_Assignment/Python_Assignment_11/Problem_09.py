# Write a program to create three lists of numbers, 
# their squares and cubes

num = int(input("Enter a number of elements : "))
list1 = []
for i in range(num):
    n = int(input(""))
    list1.append(n)
print("The given list is: ",list1)

sq_list = []
cub_list = []
for i in list1:
    sq_list.append(i**2)
    cub_list.append(i**3)
print("Square of list: ",sq_list)
print("Cube of list: ",cub_list)