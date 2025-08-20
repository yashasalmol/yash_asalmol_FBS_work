# Write a program to find sum of all elements of list

n = int(input("Enter a number : "))
list1 = []
for i in range(n):
    num = int(input(""))
    list1.append(num)
print(list1)

total = 0
for i in list1:
    total += i
print("Sum of all element : ",total)