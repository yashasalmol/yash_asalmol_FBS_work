# Write a program to remove all occurrences of a given element in the list.

list1 = [1,2,3,4,9,68,54,87,5]
x = int(input("Enter a number : "))
list2 = []
for i in list1:
    if i!=x:
        list2.append(i)
print(list2)