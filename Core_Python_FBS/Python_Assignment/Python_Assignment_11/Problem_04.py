list1 = [1,9,8,2,7,3,6,4,5]
for j in range(1,len(list1)):
    for i in range(len(list1)-j):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
print(list1[-2])