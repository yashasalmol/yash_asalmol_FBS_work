# Python Program to Find the Union of two Lists 

l1 = [10,20,10,30]
l2 = [1,2,3,4,5,2,3,2]
list1 = l1 + l2
list2 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print(list2)