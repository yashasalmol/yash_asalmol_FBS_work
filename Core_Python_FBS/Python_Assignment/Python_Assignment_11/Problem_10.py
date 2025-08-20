#  Write a program to print list after removing even numbers. 

num = int(input("Enter a number of element: "))
list1 = []
for i in range(num):
    n = int(input(""))
    list1.append(n)
print(list1)
for i in range(len(list1)):
    if list1[i]%2==0:
        print(list1[i])
