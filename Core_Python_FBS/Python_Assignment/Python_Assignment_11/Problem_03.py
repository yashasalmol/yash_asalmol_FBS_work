list3 = [[1,4,20],[3,1,90],[5,2,9],[4,3,5]]

for j in range(1,len(list3)):
    for i in range(len(list3)-j):
        if list3[i][2]>list3[i+1][2]:
            list3[i],list3[i+1]=list3[i+1],list3[i]
print(list3)