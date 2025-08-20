# Write a program to reverse the list.

num = int(input("Enter a number of elements : "))
list1 = []
for i in range(num):
    n = int(input(""))
    list1.append(n)
print(list1)
# s=list[::-1]
# print(s)
list2 = []
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print("Reversed list : ",list2)