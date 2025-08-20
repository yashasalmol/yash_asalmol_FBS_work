# Write a program to print list after removing even numbers. 

list1 = [1,2,3,4,5,6,7,8,9]
list2 = []
for i in list1:
    if i%2!=0:
        list2.append(i)
print(list2)