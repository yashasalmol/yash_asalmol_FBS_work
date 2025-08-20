# Python Program to Find the Intersection of Two Lists 

list1 = [1,2,3,4,5]
list2 = [6,7,8,9]

inserction = []

for element in list1:
    if element in list2:
        inserction.append(element)
else:
    element not in inserction
    inserction.append(element)

print(inserction)