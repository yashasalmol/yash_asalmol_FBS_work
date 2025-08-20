# Write a program to remove duplicates from the list.
list1 = [34,40,42,40,34,40,33]
list2 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print(list2)