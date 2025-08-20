# Python Program to Merge Two Lists and Sort it 

list1 = [1,5,2,4,3]
list2 = [9,6,8,7]
list3 = list1 + list2
#list3.sort()
for j in range(1,len(list3)):
    for i in range(len(list3)-j):
        if list3[i]>list3[i+1]:
            list3[i],list3[i+1]=list3[i+1],list3[i]
print(list3)