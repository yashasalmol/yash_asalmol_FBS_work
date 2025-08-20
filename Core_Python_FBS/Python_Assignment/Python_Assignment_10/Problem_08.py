'''Write a program to create a duplicate of an existing list. 
It should not point to same list.'''

list1 = [10,20,30,40,50,60]
list2 = []
for i in list1:
    list2.append(i)
print(list1)
print(list2)